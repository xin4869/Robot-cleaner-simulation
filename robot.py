from direction import Direction
from error import Error

class Robot():
    def __init__(self, name):
        self.set_name(name)
        self.world = None
        self.location = None
        self.facing = None
        self.brain = None
        self.destroyed is False
        
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
    
    def get_world(self):
        return self.world

    def set_world(self, world, location, facing):
        target_square = world.get_square(location)
        if target_square.is_empty and self.world is None:
            self.world = world
            self.location = location
            self.facing = facing
            return True
        else:
            return False
        
    def get_location(self):
        return self.location
    
    def get_location_square(self):
        return self.world.get_square(self.location)
    
    def get_facing(self):
        return self.facing
    
    def destroy(self):
        self.destroyed = True

    def fix(self):
        self.destroyed = False 
    
    def is_broken(self):
        if self.destroyed:
            print ("Robot is destroyed!")
            return True
        elif self.brain is None:
            print ("No algorithm has been set!")
            return True
        elif self.get_world() is None:
            print("No working environment set for the robot!")
            return True
        else:
            print("Robot is functioning normally!")
            return False
       
    
    def is_stuck(self):
        if not self.is_broken():
            world = self.get_world()
            current_location = self.get_location()

            for direction in Direction.direction_list:        
                target_location = current_location.get_target_coordinates(direction, 1)  
                target_square = world.get_square(target_location)
                if target_square.is_empty():
                    print("Robot functions normally!")
                    return False
            
            print("Robot is stuck!")
            return True        
                   

    def handle_stuck(self):
        if not self.is_stuck():
            return False
        
        flag = 0
        while self.is_stuck() and flag < 8:   
            new_facing = Direction.get_next_counterclockwise(self.get_facing())
            if not self.spin(new_facing):
                raise Error("Robot is broken! Cannot be spun!")
            else:
                if self.move_forward():
                    return True
                flag += 1     
            
        self.destroy()
        print("Action failed! Robot is broken!")
        return False

        
    def spin(self, new_facing):
        if self.is_broken():
            print("Robot is broken! Cannot be spun!")
            return False
        else:
            self.facing = new_facing
            return True

    
    def move(self, direction):
        if self.is_broken():
            print("Robot is broken! Cannot move!")
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

            




