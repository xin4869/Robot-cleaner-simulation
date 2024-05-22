from coordinates import Coordinates

class Square():
    def __init__(self, x=None, y=None, wall_flag = False):
        self.x = x
        self.y = y
        self.robot = None
        self.wall_flag = wall_flag      
        self.gui = None

    def get_location(self):
        return Coordinates(self.x, self.y)


    def get_robot(self):
        return self.robot
      
    def is_wall(self):
        return self.wall_flag
    

    def is_empty(self):
        return self.robot is None and not self.is_wall()
        
    
    def set_gui(self, gui):
        self.gui = gui
    
    def get_gui(self):
        return self.gui
    
    def set_wall(self):
        if self.is_empty():
            self.wall_flag = True
            return True
        else:
            return False
        
    
    # def remove_wall(self):
    #     if self.is_wall():
    #         self.wall_flag = False
    #         return True
    #     else:
    #         return False
    
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
    

