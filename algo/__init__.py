import heapq

from local_type import Vector
from maze import Maze

# Example A* pathfinder implementation that can be injected
def astar_pathfinder(
                        maze: Maze,
                        start: Vector,
                        end: Vector, 
                        heuristic,
                        print_flag: bool = False
                    ) -> list[Vector]:
    """
    A* pathfinding algorithm implementation without numpy dependencies
    
    Args:
        maze: Maze object with matrix attribute (list of lists)
        start: Starting position as Vector
        end: Target position as Vector
        heuristic: Heuristic function that takes two Vectors and returns a float
        print_flag: Whether to print debug information
        
    Returns:
        List of Vectors representing the path, or None if no path exists
    """
    # Directions: up, down, left, right
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    open_set = []
    closed_set = set()
    came_from = {}

    start_node = (start.x, start.y)
    g_score = {start_node: 0}
    f_score = {start_node: heuristic(start, end)}
    heapq.heappush(open_set, (f_score[start_node], start_node))
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == (end.x, end.y):
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(Vector(*current))
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path
            
        closed_set.add(current)
        
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Check boundaries using pure Python
            if not (0 <= neighbor[0] < len(maze.matrix[0]) and 0 <= neighbor[1] < len(maze.matrix)):
                continue
                
            # Check for walls (1) and visited nodes
            if maze.matrix[neighbor[1]][neighbor[0]] == 1 or neighbor in closed_set:
                continue
                
            # Calculate tentative g score
            tentative_g = g_score[current] + 1
            # try:
            #     if print_flag:
            #         mz_len = len(maze)  # Assuming square maze
            #         print(f"{cartesien_to_lineaire(Vector(*neighbor), mz_len)+1}: "
            #             f"h={heuristic(Vector(*neighbor), end)+1} g={tentative_g}, "
            #             f"f={heuristic(Vector(*neighbor), end) + tentative_g} "
            #             f"parent: {cartesien_to_lineaire(Vector(*current), mz_len)+1}")
            # except Exception as e:
            #     print('No print', str(e))
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(Vector(*neighbor), end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None