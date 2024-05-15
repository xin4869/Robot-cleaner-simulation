from direction import Direction

class Coordinates():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_target_coordinates(self, new_direction, distance):
        return Coordinates(self.x + new_direction[0] * distance, self.y + new_direction[1] * distance)
    
    def is_equal(self, other):
        if isinstance (other, Coordinates):
            return self.x == other.x and self.y == other.y
        return False


    def __str__(self):
        return f"({self.x}, {self.y})"
    



