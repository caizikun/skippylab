"""
Convenient operations

"""

import numpy as np
import scipy.integrate as integrate
from copy import deepcopy as copy

IMPEDANCE = 50

def average_wf(waveforms):
    """
    Get the average waveform

    Args:
        waveforms (iterable of np.ndarrays):

    Returns:
        np.ndarray
    """
    wf0 = copy(waveforms[0])
    for wf in waveforms[1:]:
        wf0 += wf

    return wf0 / float(len(waveforms))


def integrate_wf(waveform, xs, xstep,\
                 method=integrate.simps, impedance = IMPEDANCE):
    """
    Integrate a waveform, i.e. a voltage curve. If the desired result
    shall be indeed a charge, please make sure to give xs in seconds 
    and impedance in Ohm accordingly. xstep needs to be in seconds as well.

    Args:
        waveform (np.ndarray): voltage values
        xs (np.ndarray): timing values 
        xstep (float): timing bin size

    Keyword Args:
        method (func): integration method
        impedance (float): needed to calculate actual charge

    Returns:
        float
    """

    integral = method(waveform, xs, xstep)
    return integral/impedance


def save_waveform(header, waveform, filename):
    """
    save a waveform together with its header

    Args:
        header (dict): Some metainformation about the waveform
        waveform (np.ndarray): the actual voltage data
        filename (str): a filename where the data should be saved
    Returns:
        None
    """
    np.save(filename, (header, waveform))
    return None


def load_waveform(filename):
    """
    load a waveform from a file

    Args:
        filenaame (str): An existing filename

    Returns:
        tuple (dict, np.ndarray)
    """
    assert os.path.exists(filename), "File {} does not exist!".format(filename)

    if not filename.endswith(".npy"):
        filename += ".npy"

    head, wf = np.load(filename)
    return head, wf
