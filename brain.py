from robot import Robot

class Brain(Robot):
    def __init__(self, body):
        self.body = body
    

    def square_is_free(self, direction):
        current_location = self.body.get_location()
        target_location = current_location.get_target_coordinates(direction, 1)
        target_square = self.body.get_world().get_square(target_location)
        if target_square.is_empty():
            return True
        else:
            return False

    def find_direction(self):
        pass  
 
    def find_direction_home(self):
        #self.body.move(self.home_direction())
        pass

 