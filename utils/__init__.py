from collections.abc import Sequence
from typing import Optional
from local_type import Vector
from maze import Maze

def distance_manathane(a:Vector, b:Vector) -> int:
    return (abs(a.x-b.x)+abs(a.y-b.y))

def lineaire_to_cartesien (position:int, maze_width:int) -> Vector:
    return Vector(position % maze_width, position // maze_width)

def cartesien_to_lineaire (position:Vector, maze_length:int) -> int:
    return position.y*maze_length + position.x

def best_cheese_manathane(playerLocation, piecesOfCheese):
    if (len(piecesOfCheese)==0): raise Exception ('No chees')
    vmin=float('inf') # infini
    xmin=0
    for x in range(len(piecesOfCheese)):
        dist=distance_manathane(playerLocation, piecesOfCheese[x])
        if (dist<vmin):
            vmin=dist
            xmin=x
    return piecesOfCheese[xmin]