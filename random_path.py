from direction import Direction
from brain import Brain

class RandomPath(Brain):
    def __init__(self, body):
        super().__init__(body)

        self.move_body()

    def move_body(self):
        
        direction = Direction.random_direction()
        self.body.move(direction)
        self.body.spin(direction)