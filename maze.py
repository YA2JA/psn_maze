# -*- coding: utf-8 -*-

from local_type import Vector
from utils import where_2d

class Maze:
    def __init__(
                    self, 
                    matrix,
                    player,
                    finnishis
                ):
        self.matrix = matrix
        self.player = player
        self.finnishis = finnishis
    
    @staticmethod
    def load_from_file(filename:str) -> 'Maze':
        with open(filename, 'r') as file:
            maze = list(eval(file.read()))
        
        y, x = where_2d(maze, 2)[0]
        player = Vector(x, y)
        finnishis = [Vector(x, y) for (y, x) in where_2d(maze, 3)]
        return Maze(maze, player, finnishis)
    
    def get_walls(self) -> list[Vector]:
        walls = []
        for y, x in where_2d(self.matrix, 1):
            walls.append(Vector(x, y))
        return walls

    def move_player(self, target_vector:Vector):
        self.matrix[self.player.y][self.player.x] = 0
        self.matrix[target_vector.y][target_vector.x] = 2
        self.player = target_vector

    def show_walls(self):
        for line in self.matrix:
            for val in line:
                if val == 1:
                    print("X", end=' ')
                    continue
                print("-", end=' ')
            print()

    def __str__(self):
        return str(self.matrix)
    
    def __len__(self):
        return len(self.matrix[0])