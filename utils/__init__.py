from local_type import Vector

def distance_manathane(a:Vector, b:Vector) -> int:
    return (abs(a.x-b.x)+abs(a.y-b.y))

def get_movement_vector(current:Vector, target:Vector) -> Vector:
    return Vector(target.x - current.x, target.y - current.y)

def lineaire_to_cartesien (position:int, maze_width:int) -> Vector:
    return Vector(position % maze_width, position // maze_width)

def cartesien_to_lineaire (position:Vector, maze_length:int) -> int:
    return position.y*maze_length + position.x

def best_cheese_manathane(playerLocation:Vector, cheeses:list[Vector]):
    if (len(cheeses)==0): raise Exception ('No chees')
    vmin=float('inf')
    xmin=0
    for x in range(len(cheeses)):
        dist=distance_manathane(playerLocation, cheeses[x])
        if (dist<vmin):
            vmin=dist
            xmin=x
    return cheeses[xmin]

def where_2d(matrix: list[list[int]], target: int) -> list[list[int, int]]:
    """
    Find all (row, col) positions where matrix value equals target in a 2D matrix.
    
    Args:
        matrix: 2D list of any comparable values
        target: Value to search for
        
    Returns:
        List of (row, col) tuples where matrix[row][col] == target
        Empty list if no matches or empty matrix
    """
    matches = []
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == target:
                matches.append((row_idx, col_idx))
    return matches

def print_matrix(matrix, *args, **kwargs):
    for line in matrix:
        print(line)
    print(*args, **kwargs)


def signe(val:int):
    if val<0: return -1
    return 1