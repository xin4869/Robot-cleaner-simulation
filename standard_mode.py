from brain import Brain
from direction import Direction
from node import Node
import random

class StandardMode(Brain):

    def __init__(self, body):
        super().__init__(body)
        
        self.moves_remaining = 0
        self.get_random_times_move()

    def get_random_times_move(self):
        self.moves_remaining = random.randint(1, 10)

    
    def get_direction_weights(self):
        weights = []
        for direction in Direction.direction_list:
            target_inner = self.body.inner_location.get_target_coordinates(direction, 1)
            penalty = self.body.visited_inner.get(target_inner, 0)
            weights.append(1 /(1 + penalty))
            print(f"visited times {penalty} for coordinates {target_inner}")
        return weights
    
    def weighted_random_direction(self):
        weights = self.get_direction_weights()
        total_weights = sum(weights)
        normalized_weights = [w / total_weights for w in weights]
        direction = random.choices(Direction.direction_list, weights=normalized_weights, k=1)[0]
        print(f"weights {weights} of direction {direction}")
        return direction

    def find_direction(self):
        if self.moves_remaining > 0:
            direction = self.body.get_facing()
        elif self.moves_remaining == 0:
            self.get_random_times_move()
            direction = self.weighted_random_direction()
            
        if self.square_is_free(direction):
            self.body.stuck_flag = 0
            self.body.is_really_stuck = False              
            self.body.move()
            self.moves_remaining -= 1
            return
        else:
            for direction in Direction.direction_list:
                self.body.spin(direction)
                if self.square_is_free(direction):
                    self.body.stuck_flag = 0
                    self.body.is_really_stuck = False
                    self.body.move()
                    self.moves_remaining -= 1
                    return
            
            self.body.is_really_stuck = True
            self.body.stuck_flag += 1
            if self.body.stuck_flag > 6:
                self.body.destroyed = True
                return

