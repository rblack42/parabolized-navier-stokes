from __future__ import print_function, absolute_import, division
import _driver
import f90wrap.runtime
import logging

def driver(minf, rho, n):
    """
    driver(minf, rho, n)
    
    
    Defined at ../src/driver.f90 lines 1-9
    
    Parameters
    ----------
    minf : float
    rho : float array
    n : int
    
    """
    _driver.f90wrap_driver(minf=minf, rho=rho, n=n)

