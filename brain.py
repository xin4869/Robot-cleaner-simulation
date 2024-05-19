from robot import Robot
from node import Node
import copy
from coordinates import Coordinates
from direction import Direction
from error import Error

class Brain(Robot):
    def __init__(self, body):
        self.body = body
        self.end_node = self.body.init_inner_location
        self.current_node = None
        self.moving_back_flag = False

        self.open_list = []
        self.closed_list = []
        self.nodes = []
    ### when do i need to specify the body here?

    def get_node(self, position):
        for node in self.nodes:
            if node.position == position:
                return node
        return False
    
    def reset_all(self):
        self.closed_list = []
        self.open_list = []
        self.nodes = []
    
    def square_is_free(self, direction):
        self.body.target_inner_location = self.body.inner_location.get_target_coordinates(direction, 1) 
        self.body.target_location = self.body.location.get_target_coordinates(direction, 1)
        self.body.target_square = self.body.get_world().get_square(self.body.target_location)

        if self.body.target_square.is_empty():   ### no robot and no wall
            return True
        else:          
            return False
        
    # def go_home(self):    
    #     if self.body.inner_location == self.home_path[-1]:
    #         print("self.body.inner_location" , self.body.inner_location)
    #         print("self.home_path[-1]" , self.home_path[-1])
    #         direction = self.body.inner_location.get_target_direction(self.home_path[-2])
    #         self.body.spin(direction)
    #         if self.square_is_free(direction):
    #             self.home_path.pop(-1)
    #             self.body.stuck_flag = 0
    #             self.body.is_really_stuck = False
    #             self.body.move()
    #         else:
    #             self.body.stuck_flag += 1
    #             if self.body.stuck_flag >= 6:
    #                 self.body.destroyed = True

    #     else:
    #         print("self.body.inner_location" , self.body.inner_location)
    #         print("self.home_path[-1]" , self.home_path[-1])
    #         raise Error("Starting coordinates does not match!")

    def find_direction(self):
        pass
        

    def go_home(self):
        if not self.moving_back_flag:            
            if not self.get_node(self.body.inner_location):
                self.current_node = Node(None, self.body.inner_location)
                self.open_list.append(self.current_node)
                self.nodes.append(self.current_node)
                self.nodes.append(self.end_node)
            else:
                self.current_node = self.get_node(self.body.inner_location)

            print("self.current_node", self.current_node)
            print("self.open_node:")
            for open_node in self.open_list:
                print(open_node)

            self.open_list.remove(self.current_node)
            self.closed_list.append(self.current_node)

            children = []
            for direction in Direction.direction_list:
                if self.square_is_free(direction):
                    node = Node(self.current_node, self.body.target_inner_location)
                    children.append(node)
                    self.nodes.append(node)

            for child in children:
                if child in self.closed_list:
                    continue   ### skip this child
                child.g = self.current_node.g + 1
                child.h = abs(child.position.x) ** 2 + abs(child.position.y) ** 2
                child.f = child.g + child.h

                for open_node in self.open_list:
                    if child == open_node and child.g > open_node.g:
                        continue   ### skip this child

                self.open_list.append(child)

            print("self.open_list after child:")
            for open_node in self.open_list:
                print(open_node)

            self.current_node = min(self.open_list, key=lambda node: node.f)
            print("the minimal F node:", self.current_node)

        if self.body.inner_location.get_target_direction(self.current_node.position):
            self.moving_back_flag = False
            direction = self.body.inner_location.get_target_direction(self.current_node.position)
            self.body.spin(direction)
            self.square_is_free(direction)
            self.body.move()
        else:
            self.moving_back_flag = True
            actual_node = self.get_node(self.body.inner_location)
            parent_node = actual_node.parent
            diretion = self.body.inner_location.get_target_direction(parent_node.position)
            self.body.spin(diretion)
            self.square_is_free(diretion)
            self.body.move()

        return
