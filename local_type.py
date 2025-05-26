from typing import NamedTuple
import numpy.typing as npt

class Vector(NamedTuple):
    x:int
    y:int

    @staticmethod
    def from_numpy(array:npt.ArrayLike):
        return Vector(int(array[0][0]), int(array[1][0]))