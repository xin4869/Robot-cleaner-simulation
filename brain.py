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
        # self.moving_back_flag = False

        # self.open_list = []
        # self.closed_list = []
        self.nodes = []
    ### when do i need to specify the body here?

    def get_node(self, position):
        for node in self.nodes:
            if node.position == position:
                return node
        return False
    
    def reset_all(self):
        # self.closed_list = []
        # self.open_list = []
        self.nodes = []
        # self.moving_back_flag = False
    
    def square_is_free(self, direction):
        self.body.target_inner_location = self.body.inner_location.get_target_coordinates(direction, 1) 
        self.body.target_location = self.body.location.get_target_coordinates(direction, 1)
        self.body.target_square = self.body.get_world().get_square(self.body.target_location)

        if self.body.target_square.is_empty():   ### no robot and no wall
            return True
        else:          
            return False
        

    def find_direction(self):
        pass
        

    # def go_home(self):
    #     if not self.moving_back_flag:            
    #         if not self.get_node(self.body.inner_location):
    #             self.current_node = Node(None, self.body.inner_location)
    #             self.current_node.h = abs(self.body.inner_location.x) + abs(self.body.inner_location.y) 
    #             self.current_node.f = self.current_node.h + self.current_node.g
    #             self.open_list.append(self.current_node)
    #             self.nodes.append(self.current_node)
    #             self.nodes.append(self.end_node)
    #         else:
    #             self.current_node = self.get_node(self.body.inner_location)

    #         print("current_node - going to be checked children", self.current_node)
    #         print("current node g h f:", self.current_node.g, self.current_node.h, self.current_node.f)

    #         print("before removing - open:")
    #         for open_node in self.open_list:
    #             print(open_node)

    #         self.open_list.remove(self.current_node)
    #         self.closed_list.append(self.current_node)

    #         print("after removing - open:", self.open_list)
    #         print("after removing - closed:", self.closed_list)

    #         children = []
    #         for direction in Direction.direction_list:
    #             if self.square_is_free(direction):
    #                 node = Node(self.current_node, self.body.target_inner_location)
    #                 children.append(node)
    #                 self.nodes.append(node)

    #         for child in children:
    #             for closed_node in self.closed_list:
    #                 if child == closed_node:
    #                     continue   ### skip this child

    #             child.g = self.current_node.g + 1
    #             child.h = abs(child.position.x) + abs(child.position.y) 
    #             child.f = child.g + child.h

    #             for open_node in self.open_list:
    #                 if child == open_node and child.g > open_node.g:
    #                     continue   ### skip this child

    #             self.open_list.append(child)

    #         print("children g h f:")
    #         for child in children:
    #             print(child, child.g, child.h, child.f) 

    #         print("Open list after appending children:")
    #         for open_node in self.open_list:
    #             print(open_node)

    #         self.current_node = min(self.open_list, key=lambda node: node.f)
    #         print("New minimal F node:", self.current_node)

    #     direction = self.body.inner_location.get_target_direction(self.current_node.position)
    #     if direction:
    #         self.body.spin(direction)
    #         self.square_is_free(direction)
    #         self.body.move()
    #         self.moving_back_flag = False
    #         print("just next square - current inner location", self.body.inner_location)
    #     else:
    #         actual_node = self.get_node(self.body.inner_location)
    #         print("actual_node", actual_node)
    #         parent_node = actual_node.parent
    #         print("parent of actual", parent_node)
    #         diretion = self.body.inner_location.get_target_direction(parent_node.position)
    #         self.body.spin(diretion)
    #         self.square_is_free(diretion)
    #         self.body.move()
    #         self.moving_back_flag = True
    #         print("not next square yet - current inner location", self.body.inner_location)

    #     return





    def go_home(self):         
            if not self.get_node(self.body.inner_location):
                self.current_node = Node(self.body.inner_location)
                self.current_node.h = abs(self.body.inner_location.x) + abs(self.body.inner_location.y) 
                self.current_node.g += 10
                self.current_node.f = self.current_node.h + self.current_node.g
                self.nodes.append(self.current_node)
                self.nodes.append(self.end_node)
            else:
                self.current_node = self.get_node(self.body.inner_location)

            # print("current_node - going to be checked surroundings", self.current_node)
            # print("current node g h f:", self.current_node.g, self.current_node.h, self.current_node.f)

            
            surrounding_nodes = []
            for direction in Direction.direction_list:
                if self.square_is_free(direction):
                    node = self.get_node(self.body.target_inner_location)
                    if not node:
                        # print(f"node {node} not found, now creating new node")
                        node = Node(self.body.target_inner_location)
                        node.h = abs(node.position.x) + abs(node.position.y) 
        
                    node.f = node.g + node.h                      
                    surrounding_nodes.append(node)
                    self.nodes.append(node)

            # print("surrounding nodes - g h f:")
            # for node in surrounding_nodes:
                # print(node, node.g, node.h, node.f) 

            self.current_node = min(surrounding_nodes, key=lambda node: node.f)
            # print("New minimal F node/ current node:", self.current_node)
            self.current_node.g += 10
            self.current_node.f = self.current_node.g + self.current_node.h
            # print("current node g h f:", self.current_node.g, self.current_node.h, self.current_node.f)
            direction = self.body.inner_location.get_target_direction(self.current_node.position)
            self.body.spin(direction)
            self.square_is_free(direction)
            self.body.move()
            # print("just next square - current inner location", self.body.inner_location)
            return

