class Square():
    def __init__(self, wall_flag = False):
        self.robot = None
        self.wall_flag = wall_flag
        self.init = False

    def get_robot(self):
        return self.robot
    
    def is_wall(self):
        return self.wall_flag
    
    def set_init(self):
        self.init = True

    def is_init(self):
        return self.init
    
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
    

