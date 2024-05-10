from direction import Direction
from error import Error
from robotworld import RobotWorld


class Robot():
    def __init__(self, name):
        self.set_name(name)
        self.world = None
        self.location = None
        self.facing = None
        self.brain = None
        self.destroyed = False

        self.init_location = None
        self.init_facing = None

        # self.setting_algorithm = False

        self.cleaned_square = []
        
    def set_name(self, name):
        if not name:
            self.name = "Incognito"
        else:
            self.name = name

    def get_name(self):
        return self.name
    
    def set_brain(self, brain):
        self.brain = brain
    
    def get_brain(self):
        return self.brain

    # def algorithm_flag(self):
    #     return self.setting_algorithm
    
    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location
    
    def get_location_square(self):
        return self.world.get_square(self.location)
    
    def set_facing(self, facing):
        self.facing = facing
    
    def get_facing(self):
        return self.facing
    
    def set_world(self, world, location, facing):
        target_square = world.get_square(location)
        if target_square.is_empty and self.world is None:
            self.world = world
            self.location = location
            self.facing = facing
            return True
        else:
            return False
    
    def get_world(self):
        return self.world
    
    def reset(self):
        self.destroyed = False
        self.set_location(self.init_location)
        self.set_facing(self.init_facing)

        self.world.get_square(self.location).remove_robot()
        self.world.get_square(self.init_location).set_robot()
        
    def is_incomplete(self):
        if self.brain is None:
            return True
        elif self.get_world() is None:
            return True
        
    def is_stuck(self):
        if not self.is_broken():
            world = self.get_world()
            current_location = self.get_location()

            for direction in Direction.direction_list:        
                target_location = current_location.get_target_coordinates(direction, 1)  
                target_square = world.get_square(target_location)
                if target_square.is_empty():
                    return False
            return True        
                   

    def destroy(self):
        if self.is_stuck(): 
            flag = 0
            while flag < 8:
                self.is_stuck()
                flag += 1
                if not self.is_stuck():
                    return False
                
            self.destroyed = True
            return True

    def is_broken(self):
        if self.destroyed or self.is_incomplete():
            return True   
        
        
    def spin(self, new_facing):
        if self.is_broken():
            return False
        else:
            self.facing = new_facing
            return True

    
    def move(self, direction):
        if self.is_broken():
            return False
        else:
            current_square = self.get_location_square()

            target_location = self.get_location().get_target_location(direction, 1)
            target_square = self.get_world().get_square(target_location)
            
            if target_square.is_empty():
                self.location = self.get_location().get_target_coordinates(direction, 1)
                target_square.set_robot(self)
                current_square.remove_robot()
                return True
            else:
                target_square.is_empty() # print the error message defined in Square.is_empty()
                return False
            
    def move_forward(self):
        return self.move(self.get_facing())
    
    
    def act(self):
        if not self.is_broken() and not self.is_stuck():
            self.brain.move_body(self)

            




