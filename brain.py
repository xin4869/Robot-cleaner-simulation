from robot import Robot

class Brain(Robot):
    algorithms = ["Random Path", "A* Path", "Greedy Path"]
    def __init__(self, body):
        self.body = body
    
    def move_body(self):
        pass  
 
    def go_home(self):
        #self.body.move(self.home_direction())
        pass

    def home_direction(self):
        pass