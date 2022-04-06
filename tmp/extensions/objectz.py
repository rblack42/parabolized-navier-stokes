# -*- coding: utf-8 -*-
"""
============
objectzmagic
============

Magics for generating figures with ObjectZ.

.. note::

  ``ObjectZ`` and ``LaTeX`` need to be installed separately.

Usage
=====

``%%objectz``

{OBJECTZ_DOC}

"""

from __future__ import print_function
import subprocess
from builtins import str
import sys
import tempfile
from glob import glob
from os import chdir, getcwd, environ, pathsep
from subprocess import call
from shutil import rmtree, copy
from xml.dom import minidom

from IPython.core.displaypub import publish_display_data
from IPython.core.magic import (Magics, magics_class, line_magic,
                                line_cell_magic, needs_local_scope)
from IPython.testing.skipdoctest import skip_doctest
from IPython.core.magic_arguments import (
    argument, magic_arguments, parse_argstring
)
from IPython.utils.py3compat import unicode_to_str

__version__ = '0.0.1'


_mimetypes = {'png' : 'image/png',
    }

@magics_class
class ObjectZMagics(Magics):
    """A set of magics useful for creating figures with ObjectZ.
    """
    def __init__(self, shell):
        super(ObjectZMagics, self).__init__(shell)
        self._image_format = 'png'

        # Allow publish_display_data to be overridden for
        # testing purposes.
        self._publish_display_data = publish_display_data

   
    def _run_convert(self, dir):
        current_dir = getcwd()
        chdir(dir)
        call('convert -colorspace RGB objectz.pdf objectz.png', shell=True)
        chdir(current_dir)

    def _run_latex(self, code, encoding, dir):
        f = open(dir + '/objectz.tex', 'w', encoding=encoding)
        f.write(code)
        f.close()

        current_dir = getcwd()
        chdir(dir)

        ret_log = False
        log = None

        try:
            retcode = call("pdflatex --shell-escape objectz.tex", stdout=subprocess.DEVNULL, shell=True, env=env)
            if retcode != 0:
                print("LaTeX terminated with signal", -retcode, file=sys.stderr)
                ret_log = True
        except OSError as e:
            print("LaTeX execution failed:", e, file=sys.stderr)
            ret_log = True

        # in case of error return LaTeX log
        if ret_log:
            try:
                f = open('objectz.log', 'r')
                log = f.read()
                f.close()
            except IOError:
                print("No log file generated.", file=sys.stderr)

        chdir(current_dir)

        return log


    @skip_doctest
    @magic_arguments()
    @argument(
        '-sc', '--scale', action='store', type=str, default=1,
        help='Scaling factor of plots. Default is "--scale 1".'
        )
    @argument(
        '-s', '--size', action='store', type=str, default='400,240',
        help='Pixel size of plots, "width,height". Default is "--size 400,240".'
        )
        )
    @argument(
        '-p', '--package', action='store', type=str, default='',
        help='LaTeX packages to load, separated by comma, e.g., -p pgfplots,textcomp.'
        )
    @argument('-i', '--imagemagick', action='store', type=str, default='convert',
        help='Name of ImageMagick executable, optionally with full path. Default is "convert"'
        )
    @argument('--showlatex', action='store_true',
        help='Show the LATeX file instead of generating image, for debugging LaTeX errors.'
        )

    @needs_local_scope
    @argument(
        'code',
        nargs='*',
        )
    @line_cell_magic
    def tikz(self, line, cell=None, local_ns=None):
        '''
        Run TikZ code in LaTeX and plot result.

            In [9]: %tikz \draw (0,0) rectangle (1,1);

        As a cell, this will run a block of TikZ code::

            In [10]: %%tikz
               ....: \draw (0,0) rectangle (1,1);

        In the notebook, plots are published as the output of the cell.

        The size and format of output plots can be specified::

            In [18]: %%tikz -s 600,800 -f svg --scale 2
                ...: \draw (0,0) rectangle (1,1);
                ...: \filldraw (0.5,0.5) circle (.1);

        TikZ packages can be loaded with -l package1,package2[,...]::

            In [20]: %%tikz -l arrows,matrix
                ...: \matrix (m) [matrix of math nodes, row sep=3em, column sep=4em] {
                ...: A & B \\
                ...: C & D \\
                ...: };
                ...: \path[-stealth, line width=.4mm]
                ...: (m-1-1) edge node [left ] {$ac$} (m-2-1)
                ...: (m-1-1) edge node [above] {$ab$} (m-1-2)
                ...: (m-1-2) edge node [right] {$bd$} (m-2-2)
                ...: (m-2-1) edge node [below] {$cd$} (m-2-2);

        '''

        # read arguments
        args = parse_argstring(self.objectz, line)
        scale = args.scale
        size = args.size
        width, height = size.split(',')
        plot_format = args.format
        encoding = args.encoding
        latex_package = args.package.split(',')
        imagemagick_path = args.imagemagick
        picture_options = args.pictureoptions

        # arguments 'code' in line are prepended to the cell lines
        if cell is None:
            code = ''
            return_output = True
        else:
            code = cell
            return_output = False

        code = str('').join(args.code) + code

        # if there is no local namespace then default to an empty dict
        if local_ns is None:
            local_ns = {}

        # generate plots in a temporary directory
        plot_dir = '../tmp/objectz'
        add_params = ""

        if plot_format == 'png':
            add_params += "density=300,"
        tex = []
        tex.append('''
\\documentclass[border=0pt]{standalone}
''')

        tex.append('\\usepackage[oz]

        tex.append('''\\begin{document}
\\begin{%(tikz_env)s}[scale=%(scale)s,%(picture_options)s]
''' % locals())

        tex.append(code)

        tex.append('''
\\end{%(tikz_env)s}
\\end{document}
''' % locals())

        code = str('').join(tex)

        if args.showlatex:
            print(code)
            return

        latex_log = self._run_latex(code, encoding, plot_dir)
        self._run_convert(plot_dir)

        key = 'TikZMagic.Tikz'
        display_data = []

        # If the latex error log exists, then image generation has failed.
        # Publish error log and return immediately
        if latex_log:
            self._publish_display_data(source=key, data={'text/plain': latex_log})
            return

        image_filename = "%s/objectz.%s" % (plot_dir, plot_format)

        # Publish image
        try:
            image = open(image_filename, 'rb').read()
            plot_mime_type = _mimetypes.get(plot_format, 'image/%s' % (plot_format))
            width, height = [int(s) for s in size.split(',')]
            display_data.append((key, {plot_mime_type: image}))

        except IOError:
            print("No image generated.", file=sys.stderr)

        rmtree(plot_dir)

        for tag, disp_d in display_data:
            self._publish_display_data(source=tag, data=disp_d, metadata=None)


__doc__ = __doc__.format(
    OBJECTZ_DOC = ' '*8 + ObjectZMagics.objectz.__doc__,
    )


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(ObjectZMagics)
