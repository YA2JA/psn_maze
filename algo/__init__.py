import heapq


from collections.abc import Callable, Sequence
from typing import Optional
from utils import cartesien_to_lineaire
from maze import Maze
from local_type import Vector

# Example A* pathfinder implementation that can be injected
def astar_pathfinder(
                     maze: Maze,
                     start: Vector,
                     end: Vector, 
                     heuristic:Callable[[Vector, Vector], float],
                     print_flag=False
                    ) -> Optional[Sequence[Vector]]:
    """A* pathfinding algorithm implementation"""
    # Directions haut, bas, gauche, droite
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    open_set = []
    closed_set = set()
    came_from = {}

    #
    start_node = (start.x, start.y)
    g_score = {start_node: 0}
    f_score = {start_node: heuristic(start, end)}
    heapq.heappush(open_set, (f_score[start_node], start_node))
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == (end.x, end.y):
            path = []
            while current in came_from:
                path.append(Vector(*current))
                current = came_from[current]
            path.append(start)
            return path[::-1]
        closed_set.add(current)
        
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            # Check boundaries
            if not (0 <= neighbor[0] < maze.matrix.shape[1] and 0 <= neighbor[1] < maze.matrix.shape[0]):
                continue
            # Check if wall or already visited
            if maze.matrix[neighbor[1], neighbor[0]] == 1 or neighbor in closed_set:
                continue
            # Calculate tentative g score
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(Vector(*neighbor), end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
                if print_flag:
                    print(f"""
                                {cartesien_to_lineaire(Vector(*neighbor), len(maze.matrix))+1}:
                                h={heuristic(Vector(*neighbor), end)+1} g={g_score[neighbor]}, f={f_score[neighbor]}
                                parent: {cartesien_to_lineaire(Vector(*current), len(maze.matrix))+1}""".replace('\n', ' ').replace('   ', ''))
    return None