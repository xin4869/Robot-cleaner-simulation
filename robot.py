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
        self.is_really_stuck = False
        self.stuck_flag = 0
 
        self.init_location = None
        self.init_facing = None
    
        self.visited_squares = []
      

        
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
        self.set_facing(self.init_facing)

        self.world.get_square(self.location).remove_robot()
        self.world.get_square(self.init_location).set_robot()
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
        print("current square total dirts:", total)

        if total > 0: 
            if self.mode == 0:
                num_to_remove = random.randint(0, 1)
            elif self.mode == 1:
                self.battery -= 1     #####  strong mode - consume 1 battery more per move
                num_to_remove = random.randint(0, 2)
            print("num_to_remove:", num_to_remove)

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
        target_location = self.get_location().get_target_coordinates(self.get_facing(), 1)
        target_square = self.get_world().get_square(target_location)
        
        self.location = target_location
        current_square.remove_robot()
        target_square.set_robot(self)
        self.visited_squares.append(target_square)  
        self.clean()
    

        target_square_gui = target_square.get_gui()
        current_brush = target_square_gui.brush()
        current_color = target_square_gui.brush().color()
        intensity = max(current_color.alpha() - 15, 140)
        new_color = QtGui.QColor(current_color.red(), current_color.green(), current_color.blue(), intensity)       
        current_brush.setColor(QtGui.QColor(new_color))
        target_square_gui.setBrush(current_brush)
        self.world.scene.update()        ########    update scene  ????


    def act(self):
        if self.battery > 100:
            self.battery -= 1
            self.brain.find_direction()
        # elif 0 < self.battery <= 100:
        #     self.battery -= 1
        #     self.brain.find_direction_home()
        #     self.world.scene.update()
        else:
            self.destroyed = True

        


            




