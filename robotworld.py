from square import Square
from collections import Counter
from PyQt6 import QtCore

class RobotWorld:
    def __init__(self, width, height, scene=None):
        self.width = width
        self.height = height
        self.board = [[Square(x,y) for x in range(width)] for y in range(height)]
        self.robots = []
        self.dirts = []
        self.turn = 0
      
        self.scene = scene

        self.clean_level_target = None
        self.room_coverage_taget = None
        
        self.cleaned_squares = []
        self.dirty_squares = []
        self.destroyed_robots = []
  
        # self.total_visited_squares_list = []
        self.total_visited_squares = set()


    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_target_dirts(self,location):
        target_dirts = []
        for dirt in self.dirts:
            dirt_location = dirt.get_location()
            if dirt_location == location :
                target_dirts.append(dirt)
        return target_dirts
    

    def get_square(self, location):
        if self.contains(location):
            return self.board[location.get_y()][location.get_x()]
        else:
            return Square(wall_flag=True)
    
    def get_all_squares(self):
        all_squares = [square for row in self.board for square in row]
        return all_squares
    
    # def count_visit(self):
    #     visit_dict = Counter(self.total_visited_squares_list)
    #     return visit_dict

    
    def update_total_visited_squares(self):       
        for robot in self.robots:
            for square in robot.visited_squares:
                self.total_visited_squares.add(square)
        
        # self.total_visited_squares = set(self.total_visited_squares_list)
        # self.total_visited_squares.update(self.total_visited_squares_list)


    def get_room_coverage(self):
        self.update_total_visited_squares()
        room_coverage = len(self.total_visited_squares) / len(self.get_all_squares())

        return room_coverage
    
    def get_clean_level(self):
        if len(self.total_visited_squares) == 0:
            clean_level = 0
        else:
            clean_level = len(self.cleaned_squares) / len(self.total_visited_squares)

        return clean_level

    def get_board(self):
        return self.board
    
    # def add_robot(self, robot, location, facing):
    #     if robot.set_world(self, location, facing):
    #         self.robots.append(robot)
    #         self.get_square(location).set_robot(robot)
    #         return True
    #     else:
    #         return False
        
    # def remove_robot(self, robot):
    #     if robot in self.robots:
    #         self.robots.remove(robot)
    #         self.get_square(robot.get_location()).remove_robot()
    #         return True
    #     else:
    #         return False
        
        
    def add_wall(self, location):
        return self.get_square(location).set_wall()
    
    # def remove_wall(self, location):
    #     return self.get_square(location).remove_wall()


    def contains(self, coordinates):
        x = coordinates.get_x()
        y = coordinates.get_y()
        return 0 <= x < self.width and 0 <= y < self.height
    

    def get_number_of_robots(self):
        return len(self.robots)
    
  
    def take_turn(self):
        if self.get_number_of_robots() > 0:
            current = self.robots[self.turn]
            if current is not None:
                if not current.destroyed:
                    current.act()
                else:
                    if current not in self.destroyed_robots:
                        self.destroyed_robots.append(current)
                self.turn = (self.turn + 1) % self.get_number_of_robots()

  


        