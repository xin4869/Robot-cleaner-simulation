class Square():
    def __init__(self, is_wall = False):
        self.robot = None
        self.is_wall = is_wall

    def get_robot(self):
        return self.robot
    
    def is_wall_square(self):
        return self.is_wall
    
    def is_empty(self):
        if self.is_wall:
            print ("Wall Square - cannot move!")
            return False
        else:
            if self.robot is not None:
                print ("Occupied square - cannot move!")
                return False
            else:
                return True
    
    
    def set_wall(self):
        if self.is_empty:
            self.is_wall = True
            return True
        else:
            return False
    
    def remove_wall(self):
        if self.is_wall:
            self.is_wall = False
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
    

