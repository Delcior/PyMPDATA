from functools import lru_cache
import numba
from PyMPDATA.impl.enumerations import SIGN_RIGHT, SIGN_LEFT


@lru_cache()
def _make_scalar(at):
    @numba.njit()
    def fill_halos(psi, n, sign):
        return at(*psi, sign * n)
    return fill_halos


@lru_cache()
def _make_vector(at):
    @numba.njit()
    def fill_halos(psi, n, sign):
        return at(*psi, sign * n)
    return fill_halos


class Periodic:
    def __init__(self):
        assert SIGN_RIGHT == -1
        assert SIGN_LEFT == +1

    def make_scalar(self, at, halo, dtype):
        return _make_scalar(at)

    def make_vector(self, at, dtype):
        return _make_vector(at)
