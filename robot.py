from direction import Direction
from error import Error
from robotworld import RobotWorld
from coordinates import Coordinates
import random
from PyQt6 import QtGui

class Robot():
    def __init__(self, name):
        self.set_name(name)
        self.world = None
        self.facing = None
        self.brain = None
        self.mode = 0
        self.battery = 1000

        self.location = None
        self.target_location = None
        self.target_square = None

        # self.inner_map = {Coordinates(0,0)}
        self.init_inner_location = Coordinates(0,0)
        self.inner_location = None
        self.target_inner_location = None

        self.destroyed = False
        self.is_really_stuck = False
        self.stuck_flag = 0
 
        self.init_location = None
        self.init_facing = None
    
        self.visited_squares = set()
 
        
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
    
    def set_inner_location(self, location):
        self.inner_location = location

    def get_inner_location(self):
        return self.inner_location
    
    # def inner_set_wall(self, coordinates):
    #     if coordinates not in self.inner_map:
    #         self.inner_map[coordinates] = 1

    # def inner_set_free(self, coordinates):
    #     if coordinates not in self.inner_map:
    #         self.inner_map[coordinates] = 0

    def get_location_square(self):
        return self.world.get_square(self.location)
    
    def set_facing(self, facing):
        self.facing = facing
    
    def get_facing(self):
        return self.facing
    
    # def set_world(self, world, location, facing):
    #     target_square = world.get_square(location)
    #     if target_square.is_empty and self.world is None:
    #         self.world = world
    #         self.location = location
    #         self.facing = facing
    #         return True
    #     else:
    #         return False

    def set_world(self, world):
        self.world = world
    
    def get_world(self):
        return self.world
    
    def reset(self):
        self.destroyed = False
        self.set_location(self.init_location)
        self.set_inner_location(self.init_inner_location)
        self.set_facing(self.init_facing)
        self.battery = 1000
        self.stuck_flag = 0
        self.is_really_stuck = False

        self.world.get_square(self.location).remove_robot()
        self.world.get_square(self.init_location).set_robot(self)
        self.world.destroyed_robots.remove(self)
        
    def is_incomplete(self):
        if self.brain is None or self.world is None:
            return True
        else:
            return False

        
    def is_stuck(self):
        return self.is_really_stuck
                   

    def is_broken(self):
        if self.destroyed or self.is_incomplete():
            return True   
        
        
    def spin(self, direction):
        self.facing = direction

    def clean(self):
        current_square = self.world.get_square(self.location)
        target_dirts = self.world.get_target_dirts(self.location)
        total = len(target_dirts)

        if total > 0: 
            if self.mode == 0:
                num_to_remove = random.randint(0, 1)
            elif self.mode == 1:
                self.battery -= 1     #####  strong mode - consume 1 battery more per move
                num_to_remove = random.randint(0, 2)

            if num_to_remove > total:
                num_to_remove = total

            for _ in range(num_to_remove):
                if len(target_dirts) > 1:
                    removed_dirt = target_dirts.pop(random.randint(0, len(target_dirts) - 1))
                else:
                    removed_dirt = target_dirts.pop(0)
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


    def move(self):
    
        current_square = self.get_location_square()
        current_square.remove_robot()
        self.location = self.target_location 
        self.inner_location = self.target_inner_location    
        self.target_square.set_robot(self)  
        self.visited_squares.add(self.target_square)   ### add to set (set - always unique)
        self.clean()
    
        target_square_gui = self.target_square.get_gui()
        current_brush = target_square_gui.brush()
        current_color = target_square_gui.brush().color()
        intensity = max(current_color.alpha() - 15, 140)
        new_color = QtGui.QColor(current_color.red(), current_color.green(), current_color.blue(), intensity)       
        current_brush.setColor(QtGui.QColor(new_color))
        target_square_gui.setBrush(current_brush)
        # self.world.scene.update()        ########    update scene  ????


    def act(self):
        if not self.is_broken():
            if self.battery > 100:
                self.battery -= 1
                self.brain.find_direction()
        
            elif 0 < self.battery <= 100:
                if not self.inner_location == self.init_inner_location:
                    self.battery -= 1           
                    self.brain.go_home() 
                else:
                    self.battery = 1000
                    self.brain.reset_all()                            
            else:
                self.destroyed = True

        


            




