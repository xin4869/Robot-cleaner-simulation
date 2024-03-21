class Square():
    def __init__(self, is_wall = False):
        self.robot = None
        self.is_wall = is_wall

    def get_robot(self):
        return self.robot
    
    def is_wall_square(self):
        return self.is_wall
    
    def is_empty(self):
        return not self.is_wall and self.robot is None
    
    def set_wall(self):
        if self.is_empty:
            self.is_wall = True
            return True
        else:
            return False
    
    def set_robot(self, robot):
        if self.is_empty:
            self.robot = robot
            return True
        else:
            return False
        
    def remove_robot(self):
        removed_robot = self.robot
        self.robot = None
        return removed_robot
    

