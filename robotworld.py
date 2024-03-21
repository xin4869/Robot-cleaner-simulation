from square import Square

class RobotWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[Square() for x in range(width)] for y in range(height)]
        self.robots = []
        self.turn = 0



    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_square(self, location):
        return self.board[location.get_y()][location.get_x()]
    
    def add_robot(self, robot, location, facing):
        if robot.set_world(self, location, facing):
            self.robots.append(robot)
            self.get_square(location).set_robot(robot)
            return True
        else:
            return False
        

     
