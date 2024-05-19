from direction import Direction
from brain import Brain

class RandomPath(Brain):
    def __init__(self, body):
        super().__init__(body)

    def find_direction(self):      
        direction = Direction.random_direction()    
        self.body.spin(direction)      
        if self.square_is_free(direction):
            self.body.stuck_flag = 0
            self.body.is_really_stuck = False              
            self.body.move()
        else:
            for direction in Direction.direction_list:
                self.body.spin(direction)
                if self.square_is_free(direction):
                    self.body.stuck_flag = 0
                    self.body.is_really_stuck = False
                    self.body.move()
                    return
            
            self.body.is_really_stuck = True
            self.body.stuck_flag += 1
            if self.body.stuck_flag > 6:
                self.body.destroyed = True

        

######  now everytime after a move, update the robot direction_map