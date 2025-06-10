#!/usr/bin/env pybricks-micropython

from maze import Maze
from utils import (
                    cartesien_to_lineaire,
                    distance_manathane,
                    get_movement_vector
                )

from algo import astar_pathfinder
from hardware.demo import move, current_angle, turn_to, gyro
from local_type import Vector
import time

def main():
    maze = Maze.load_from_file('./mazes/level1.txt')

    # 1 exo
    length=len(maze)
    print(length)
    print(
            cartesien_to_lineaire(maze.player, length)+1,
            cartesien_to_lineaire(maze.finnishis[0], length)
        )
    for vec in maze.get_walls():
        print(cartesien_to_lineaire(vec, length)+1, end=' ')
    print()

    # 2 exo
    maze.show_walls()

    # Find path
    path = astar_pathfinder(maze, maze.player, maze.finnishis[0], distance_manathane)
    
    #Mesure wheels::
    # if True:
    #     import hardware.wheel

    #exo 3
    # Move player to finnish
    for vec in path:
        goto = get_movement_vector(maze.player, vec)
        move(goto)
        # print(goto.x, goto.y)
        maze.player = vec

    # for i in (270, 360, 90, 180, 90, 0, 180):
    #     print("Angle:", current_angle, "calculeted", gyro.angle())
    #     turn_to(i)
    #     time.sleep(3)

if __name__ == "__main__":
    main()