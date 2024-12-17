from src.summlib.operations import cumsum
import numpy as np


def test_cumsum():
    array = np.array([1,2,3])
    assert np.allclose(cumsum(array),np.array([1,3,6]))
