from robot import Robot

class Brain(Robot):
    def __init__(self, body):
        self.body = body
    ### when do i need to specify the body here?

    def square_is_free(self, direction):
        self.target_inner_location = self.inner_location.get_target_coordinates(direction, 1) 
        self.target_location = self.location.get_target_coordinates(direction, 1)
        self.target_square = self.body.get_world().get_square(self.target_location)

        if self.target_square.is_empty():
            self.body.inner_set_free(self.target_inner_location)
            return True
        else:
            if self.target_square.is_wall():
                self.body.inner_set_wall(self.target_inner_location)
            else:
                self.body.inner_set_free(self.target_inner_location)              
            return False

    def find_direction(self):
        pass  
 
    def find_direction_home(self):
        #self.body.move(self.home_direction())
        pass
