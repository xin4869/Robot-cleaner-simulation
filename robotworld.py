from square import Square
from collections import Counter

class RobotWorld:
    def __init__(self, width, height, scene=None):
        self.width = width
        self.height = height
        self.board = [[Square() for x in range(width)] for y in range(height)]
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
            if dirt_location.is_equal(location):
                target_dirts.append(dirt)
        return target_dirts
    
    def get_square(self, location):
        if self.contains(location):
            return self.board[location.get_y()][location.get_x()]
        else:
            return Square(True)
    
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
            print(f"take_turn() called, current robot going to take a turn has turn number  {self.turn}")
            current = self.robots[self.turn]
            if current is not None:
                if not current.destroyed:
                    current.act()
                    print("robot act() has been called")
                else:
                    if current not in self.destroyed_robots:
                        self.destroyed_robots.append(current)
                self.turn = (self.turn + 1) % self.get_number_of_robots()
                print(f"turn number has been added 1, now it is {self.turn}")

    def take_turn_all(self):
        for _ in range(self.get_number_of_robots()):
            print(f"{_}th (take_turn) in range (len(world.robots)):{len(self.robots)}")
            self.take_turn()


    def start_cleaning(self):
        room_coverage = self.get_room_coverage()
        clean_level = self.get_clean_level()
        #### test 
        print("room coverage: ", room_coverage)
        print("clean level: ", clean_level)
        self.take_turn_all()
        #### test

        # while room_coverage < self.room_coverage_taget or clean_level < self.clean_level_target:
        #     self.take_turn_all()
        #     if len(self.destroyed_robots) == len(self.robots):
        #         break
            

            



        