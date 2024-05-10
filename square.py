class Square():
    def __init__(self):
        self.robot = None
        self.dirts_per_square = []
        self.wall_flag = False

    def get_robot(self):
        return self.robot
    
    def is_wall(self):
        return self.wall_flag
    

    def is_empty(self):
        if self.is_wall():
            return False
        else:
            if self.robot is not None:
                return False
            else:
                return True
    
    
    def set_wall(self):
        if self.is_empty():
            self.wall_flag = True
            return True
        else:
            return False
        
    
    def remove_wall(self):
        if self.is_wall():
            self.wall_flag = False
            return True
        else:
            return False
    
    def set_robot(self, robot):
        if self.is_empty():
            self.robot = robot
            return True
        else:
            return False
        
    def remove_robot(self):
        removed_robot = self.robot
        self.robot = None
        return removed_robot
    

