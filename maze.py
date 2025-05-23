# -*- coding: utf-8 -*-

from collections.abc import Sequence
from dataclasses import dataclass
from local_type import Vector

import numpy as np
import numpy.typing as npt

@dataclass
class Maze:
    matrix: npt.NDArray[npt.NDArray[np.int32]]
    player: Vector
    cheeses: Sequence[Vector]

    @staticmethod
    def load_from_file(filename:str) -> 'Maze':
        with open(filename, 'r') as file:
            maze = np.array(eval(file.read()))
        player = Vector.from_numpy(np.where(maze == 2)[::-1])
        cheeses = [Vector(x, y) for y, x in zip(*np.where(maze == 3))]
        return Maze(maze, player, cheeses)
    
    def get_walls(self) -> Sequence[Vector]:
        array = []
        for i, j in zip(*np.where(self.matrix == 1)):
            array.append(Vector(j, i))
        return array

    def move_player(self, target_vector:Vector):
        self.matrix[self.player.y][self.player.x] = 0
        self.matrix[target_vector.y][target_vector.x] = 2
        self.player = target_vector

    def __str__(self):
        return str(self.matrix)
    
    def __len__(self):
        return len(self.matrix)

    def print_walls(self):
        text = ''
        for i in np.where(self.matrix == 1, "x", "-"):
            text+=' '.join(i)
            text+='\n'
        print(text)
        return text