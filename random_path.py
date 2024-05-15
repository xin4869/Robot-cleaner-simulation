from direction import Direction
from brain import Brain

class RandomPath(Brain):
    def __init__(self, body):
        super().__init__(body)

    def find_direction(self):      
        if not self.body.is_broken():
            direction = Direction.random_direction()          
            if self.square_is_free(direction):
                self.body.stuck_flag = 0
                self.body.is_really_stuck = False
                self.body.spin(direction)
                self.body.move()
            else:
                for direction in Direction.direction_list:
                    print(direction)
                    self.body.spin(direction)
                    if self.square_is_free(direction):
                        self.body.stuck_flag = 0
                        self.body.is_really_stuck = False
                        self.body.move()
                        return
                
                self.body.is_really_stuck = True
                self.body.stuck_flag += 1
                print(self.body.stuck_flag)
                if self.body.stuck_flag > 15:
                    self.body.destroyed = True

        

