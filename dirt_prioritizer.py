from brain import Brain
from direction import Direction

class DirtPrioritizer(Brain):
    def __init__(self, body):
        super().__init__(body) 
                 
    def find_direction(self):
        if not self.deep_clean:
            nearby_spots = {}
            for direction in Direction.direction_list:    
                if self.square_is_free(direction):               
                    penalty = self.body.visited_inner.get(self.body.target_inner_location, 0)
                    nearby_spots[direction] = penalty

            if nearby_spots:
                self.body.is_really_stuck = False
                self.body.stuck_flag = 0               

                direction = min(nearby_spots, key=nearby_spots.get)               
                self.body.spin(direction)
                self.square_is_free(direction)
                self.body.move()
                return

            else:
                self.body.is_really_stuck = True
                self.body.stuck_flag += 1
                if self.body.stuck_flag > 6:
                    self.body.destroyed = True
                    return
        else:
            self.body.clean()

                        