from direction import Direction
from error import Error
from robotworld import RobotWorld
import random
from PyQt6 import QtGui

class Robot():
    def __init__(self, name):
        self.set_name(name)
        self.world = None
        self.location = None
        self.facing = None
        self.brain = None
        self.mode = 0
        self.battery = 1000

        self.destroyed = False
 
        self.init_location = None
        self.init_facing = None

        self.exit_direction = None
        self.stuck_flag = 0
        self.visited_squares = []
      

        # self.setting_algorithm = False

        
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
        if self.brain is None or self.world is None:
            return True
        else:
            return False

        
    def is_stuck(self):
        if not self.is_broken():
            world = self.get_world()
            current_location = self.get_location()

            for direction in Direction.direction_list:        
                target_location = current_location.get_target_coordinates(direction, 1)  
                target_square = world.get_square(target_location)
                if target_square.is_empty():
                    self.exit_direction = direction
                    return False
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

    def clean(self):
        current_square = self.world.get_square(self.location)
        target_dirts = self.world.get_target_dirts(self.location)
        total = len(target_dirts)
        if total > 0: 
            if self.mode == 0:
                num_to_remove = random.randint(1, 3)
            elif self.mode == 1:
                self.battery -= 1     #####  strong mode - consume 1 battery more per move
                num_to_remove = random.randint(2, 4)

            for _ in range(num_to_remove):
                removed_dirt = target_dirts.pop(random.randint(0, len(target_dirts) - 1))
                self.world.dirts.remove(removed_dirt)
                self.world.scene.removeItem(removed_dirt.get_dirt_gui())
                self.world.scene.update()        ########## UPDATE SCENE?????
                del removed_dirt

            if num_to_remove >= total:
                if current_square not in self.world.cleaned_squares:
                    self.world.cleaned_squares.append(current_square)
                    if current_square in self.world.dirty_squares:
                        self.world.dirty_squares.remove(current_square)    ##### pop - index, remove - specific value
            else:
                if current_square not in self.world.dirty_squares:
                    self.world.dirty_squares.append(current_square)
        else:
            if current_square not in self.world.cleaned_squares:
                self.world.cleaned_squares.append(current_square)


    def move(self, direction):
        if self.is_broken():
            return False
        else:
            self.spin(direction)
            current_square = self.get_location_square()

            target_location = self.get_location().get_target_coordinates(direction, 1)
            target_square = self.get_world().get_square(target_location)
            
            if target_square.is_empty():
                self.location = target_location
                target_square.set_robot(self)  
                target_square_gui = target_square.get_gui()
                current_brush = target_square_gui.brush()
                current_color = target_square_gui.brush().color()

                if target_square not in self.visited_squares:                  
                    new_color = QtGui.QColor(230, 230, 230)         ########## first time visit - change to purple
                else:
                    intensity = min(current_color.alpha() + 20, 255)
                    new_color = QtGui.QColor(current_color.red(), current_color.green(), current_color.blue(), intensity)

                current_brush.setColor(QtGui.QColor(new_color))
                target_square_gui.setBrush(current_brush)
                self.world.scene.update()        ########    update scene  ????

                self.visited_squares.append(target_square)
                current_square.remove_robot()
                self.clean()
                return True
            else:
                # if self.is_stuck():
                #     self.destroy()                          
                # if self.exit_direction is not None:  
                if not self.is_stuck():                 
                    current_square.remove_robot()
                    self.spin(self.exit_direction)
                    exit_location = self.get_location().get_target_coordinates(self.exit_direction, 1)
                    self.location = exit_location
                    exit_square = self.get_world().get_square(exit_location)
                    exit_square.set_robot(self)
                    
                else:                                           
                    self.stuck_flag += 1
                    if self.stuck_flag > 5:
                        self.destroyed = True
                      
            
    def move_forward(self):
        return self.move(self.get_facing())
    

    def act(self):
            if not self.is_broken():
                if self.battery > 100:
                    self.battery -= 1
                    self.brain.move_body()
                    self.world.scene.update()
                elif 0 < self.battery <= 100:
                    self.battery -= 1
                    self.brain.go_home()
                    self.world.scene.update()
                else:
                    self.destroyed = True


            




