from maze import Maze
from utils import distance_manathane
from algo import astar_pathfinder

def main():
    maze = Maze.load_from_file('mazes/level1.txt')
    # 1 exo
    # print(length:=len(maze.matrix))
    # print(
    #         cartesien_to_lineaire(maze.player, length)+1,
    #         cartesien_to_lineaire(maze.cheeses[0], length)+1
    # )

    # for vec in maze.get_walls():
    #     print(cartesien_to_lineaire(vec, length)+1, end=' ')
    # print()
    
    # 2 exo
    # print(maze)
    # astar_pathfinder (print_flag)
    maze.print_walls()
    path = astar_pathfinder(maze, maze.player, maze.cheeses[0], distance_manathane)
    for vec in path:             
        maze.move_player(vec)
        print(maze, "\n")
if __name__ == "__main__":
    main()