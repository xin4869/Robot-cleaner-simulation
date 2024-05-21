from brain import Brain
from direction import Direction
from node import Node
import random

class StandardMode(Brain):

    def __init__(self, body):
        super().__init__(body)

    def find_direction(self):
        nearby_spots = {}       
        for direction in Direction.direction_list:    
            if self.square_is_free(direction):               
                penalty = self.body.visited_inner.get(self.body.target_inner_location, 0)
                nearby_spots[direction] = penalty
            
        if nearby_spots:
            direction = min(nearby_spots, key=nearby_spots.get)
            self.body.spin(direction)
            self.body.stuck_flag = 0
            self.body.is_really_stuck = False
            self.square_is_free(direction)
            self.body.move()
            return

        else:
            self.body.is_really_stuck = True
            self.body.stuck_flag += 1
            if self.body.stuck_flag > 6:
                self.body.destroyed = True
                return
                
                   


