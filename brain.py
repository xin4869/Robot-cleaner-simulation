from robot import Robot

class Brain(Robot):
    algorithms = ["Random Path", "A* Path", "Greedy Path"]
    def __init__(self, body):
        self.body = body
    
    def move_body(self):
        pass  

    def sensor(self):
        pass