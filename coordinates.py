from direction import Direction

class Coordinates():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (x, y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_target_coordinates(self, new_direction, distance):
        return Coordinates(self.x + new_direction[0] * distance, self.y + new_direction[1] * distance)
    
    def get_target_direction(self, new_coordinates):
        if new_coordinates.x == self.x:
            if new_coordinates.y > self.y:
                return Direction.south
            elif new_coordinates.y < self.y:
                return Direction.north
        elif new_coordinates.y == self.y:
            if new_coordinates.x > self.x:
                return Direction.east
            elif new_coordinates.x < self.x:
                return Direction.west

        else:
            return False
    # def is_equal(self, other):
    #     if isinstance (other, Coordinates):
    #         return self.x == other.x and self.y == other.y
    #     return False
    
    def __eq__(self, other):
        if not isinstance(other, Coordinates):
            return False
        return self.x == other.x and self.y == other.y


    def __str__(self):
        return f"({self.x}, {self.y})"
    



