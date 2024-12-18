from src.summlib.operations import cumsum, readfile
import numpy as np


def test_cumsum():
    array = np.array([1,2,3])
    assert np.allclose(cumsum(array),np.array([1,3,6]))


def test_readline():
    readfile()
