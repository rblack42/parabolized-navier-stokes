import ctypes

from ctypes import c_bool, c_int, c_float, byref, POINTER, cdll

here = os.path.abspath(os.path.dirname(__file__))
lib_path = os.path.join(heer, 'build','librrbaxi.dylib')
lib_ext = lib_path[lib_path.rfind(','):]

class PyRRBxi(object):
    """Python interface to rrbaxi library"""

    def __init__(self):
        

