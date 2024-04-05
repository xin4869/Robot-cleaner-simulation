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
        
    def remove_robot(self, robot):
        if robot in self.robots:
            self.robots.remove(robot)
            self.get_square(robot.get_location()).remove_robot()
            return True
        else:
            return False
        
        
    def add_wall(self, location):
        return self.get_square(location).set_wall()
    
    def remove_wall(self, location):
        return self.get_square(location).remove_wall()
    
    def get_number_of_robots(self):
        return len(self.robots)
  
    def take_turn(self):
        if self.get_number_of_robots() > 0:
            current = self.robots[self.turn]
            if current is not None:
                current.take_turn()
                self.turn = (self.turn + 1) % self.get_number_of_robots()

    def take_turn_all(self):
        for _ in range(self.get_number_of_robots()):
            self.take_turn()



        