from direction import Direction
from brain import Brain

class RandomPath(Brain):
    def __init__(self, body):
        super().__init__(body)

    def move_body(self):     
        direction = self.determine_direction()
        current_location = self.body.get_location()
        target_location = current_location.get_target_coordinates(direction, 1)
        while not self.body.get_world().contains(target_location):
            direction = Direction.random_direction()
        self.body.move(direction)  

    def determine_direction(self):
        direction = Direction.random_direction()
        current_location = self.body.get_location()

        return direction

        

        #### if stuck:  ?????