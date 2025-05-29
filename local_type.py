class Vector:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def __eq__(self:'Vector', other:'Vector'):
        return self.x == other.x and self.y == other.y
    
    def __add__(self:'Vector', other:'Vector'):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self:'Vector', other:'Vector'):
        return Vector(self.x - other.x, self.y - other.y)