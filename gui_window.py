from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QPen

from coordinates import Coordinates
from robotworld import RobotWorld
from robot import Robot
from direction import Direction
from square import Square
from dirt import Dirt
from brain import Brain
from random_path import RandomPath
from rules import Rules

from gui_robot import GuiRobot

import random

class GuiWindow(QtWidgets.QMainWindow):
   
    def __init__(self, square_size):
        super().__init__()
        self.added_robot_gui = []
        self.world = None
        self.square_size = square_size

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.main_layout)

        self.init_rules_bt()
        self.init_world_bt()

        self.button_layout = QtWidgets.QVBoxLayout()

        self.button_layout.addWidget(self.button_rules)
        self.button_layout.addWidget(self.button_initworld)    

        self.main_layout.addLayout(self.button_layout)

        self.grid_drawn = False
        self.obs_added = False
        self.obs_bt_clicked = False
        self.added_obs_amount = 0
        self.world_finalized = False

        self.adding_robot = False
        self.adding_obs = False

        self.clicked_x = None
        self.clicked_y = None

        self.new_robot = None

        self.init_window()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_gui_robots)
        self.timer.start(10)
        

    def init_window(self):
        self.setGeometry(1000, 500, 1200, 850)

        self.setWindowTitle('Robot World')
        
        self.scene = QtWidgets.QGraphicsScene()
        # self.scene.setSceneRect(0, 0, 1200, 850)

        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.main_layout.addWidget(self.view)

        self.show()
    
    def get_scene(self):
        return self.scene
    
    def change_bt_color(self, button):
        button.setStyleSheet("background-color: green")
    
    def change_bt_color_back(self, button):
        button.setStyleSheet("")


    def init_rules_bt(self):
        self.button_rules = QtWidgets.QPushButton('Rules', self)
        self.button_rules.clicked.connect(lambda: self.change_bt_color(self.button_rules))
        self.button_rules.clicked.connect(self.read_rules)
        

    def read_rules(self):
        info_box = Rules(self)
        info_box.finished.connect(lambda: self.change_bt_color_back(self.button_rules))
        info_box.exec()

        
    def init_world_bt(self):
        self.button_initworld = QtWidgets.QPushButton('Initialize grid', self)
        self.button_initworld.clicked.connect(lambda: self.change_bt_color(self.button_initworld))
        self.button_initworld.clicked.connect(self.create_world)
        
        
    def create_world(self):
        # text,ok = QtWidgets.QInputDialog.getMultiLineText(self, 'Create Robot World', 'Enter world width dimension, Max: 20:')
        # if ok:
        #     if text == "":
        #         QtWidgets.QMessageBox.warning(self, "Error", "Please enter width dimensions!")
        #         self.change_bt_color_back(self.button_initworld)
        #     elif text.isdigit() == False: 
        #         QtWidgets.QMessageBox.warning(self, "Error", "Please enter only numeric values!")
        #         self.change_bt_color_back(self.button_initworld)
        #     else:
        #         width = int(text)
        #         text,ok = QtWidgets.QInputDialog.getMultiLineText(self, 'Create Robot World', 'Enter world height dimension, Max: 15')
                # if ok:
        #             if text == "":
        #                 QtWidgets.QMessageBox.warning(self, "Error", "Please enter height dimensions!")
        #                 self.change_bt_color_back(self.button_initworld)
        #             elif text.isdigit() == False: 
        #                 QtWidgets.QMessageBox.warning(self, "Error", "Please enter only numeric values!")
        #                 self.change_bt_color_back(self.button_initworld)
        #             else:
        #                 height = int(text)
                        width = 10
                        height = 8
                        self.world = RobotWorld(width, height)
                        #QtWidgets.QMessageBox.information(self, "Success", "Robot World initialized successfully!")
                        # msg_box = QtWidgets.QMessageBox()
                        # msg_box.setText("Robot World initialized successfully!")
                        # msg_box.exec()
                        self.draw_grid()
                        self.grid_drawn = True
                        
                        self.init_bot_bt()
                        self.init_obs_bt()
                        self.init_finalize_bt()

                        self.button_layout.removeWidget(self.button_initworld)
                        self.button_initworld.deleteLater()
                # else:
                #     self.change_bt_color_back(self.button_initworld)
            # else:
            #     self.change_bt_color_back(self.button_initworld)


    def draw_grid(self):
        for y in range(self.world.get_height()):
            for x in range(self.world.get_width()):              
                x_gui = x * self.square_size
                y_gui = y * self.square_size
                square_gui = QtWidgets.QGraphicsRectItem(x_gui, y_gui, self.square_size, self.square_size)

                square = self.world.get_square(Coordinates(x, y))    

                square_gui.setBrush(QtGui.QColor(255, 255, 255))

                self.scene.addItem(square_gui)  
                self.scene.setSceneRect(self.scene.itemsBoundingRect())
                self.view.adjustSize()
                self.view.show()
                # self.adjustSize()


    def init_obs_bt(self):
        if self.grid_drawn:
            self.button_initobs = QtWidgets.QPushButton('Place obstacle', self)

            self.button_initobs.clicked.connect(self.add_obstacle)

            self.button_layout.addWidget(self.button_initobs)

    def add_obstacle(self):
        if self.grid_drawn:
            #QtWidgets.QMessageBox.information(self, "Add obstacle", "Please click on the square in which you want to place the obstacle.")
            # self.adding_obs = True
            self.adding_robot = False
            self.obs_bt_clicked = True

    def draw_obs(self, coordinates):
        if self.grid_drawn:
            square = self.world.get_square(coordinates)
            if square.is_wall(): 
                x_gui = coordinates.get_x() * self.square_size
                y_gui = coordinates.get_y() * self.square_size

                square_gui = QtWidgets.QGraphicsRectItem(x_gui, y_gui, self.square_size, self.square_size)
                
                brush = QtGui.QBrush(QtCore.Qt.BrushStyle.Dense3Pattern)   ####### what are QtGui, QtCore, and Qt? Difference?
                brush.setColor(QtGui.QColor(0, 0, 0))
                square_gui.setBrush(brush)

                self.scene.addItem(square_gui)

    def init_bot_bt(self):
        if self.grid_drawn:
            self.button_initbot = QtWidgets.QPushButton('Add Robot', self)

            self.button_initbot.clicked.connect(lambda: self.change_bt_color(self.button_initbot))
            self.button_initbot.clicked.connect(self.add_to_world)

            self.button_layout.addWidget(self.button_initbot)


    def add_to_world(self):
        
        name, ok = QtWidgets.QInputDialog.getText(self, 'Initialize Robot', 'Enter robot name:')
        if ok:
            while name in [robot.get_name() for robot in self.world.robots]:
                response = QtWidgets.QMessageBox.warning(self, "Error", f"Robot {name} has already been added!")               
                name, ok = QtWidgets.QInputDialog.getText(self, 'Initialize Robot', 'Enter robot name:')
                if not ok:
                    self.change_bt_color_back(self.button_initbot)
                    return     
            new_robot = Robot(name)      


            direction, ok = QtWidgets.QInputDialog.getText(self, "Initialize robot direction", f"Which direction should Robot {name} face? Enter one of these: N, S, E, W (North, South, East, West).")       
            if ok:
                while direction.lower() not in ["n", "s", "e", "w"]:
                    response = QtWidgets.QMessageBox.warning(self, "Error", "Invalid direction! Please enter a valid direction.")            
                    direction, ok = QtWidgets.QInputDialog.getText(self, "Initialize robot direction", f"Which direction should Robot {name} face? Enter one of these: N, S, E, W")                 
                    if not ok:
                        self.change_bt_color_back(self.button_initbot)
                        return
                    
                if direction.lower() == "n":
                    new_robot.init_facing = Direction.north
                    new_robot.set_facing(Direction.north)    
                elif direction.lower() == "s":
                    new_robot.init_facing = Direction.south
                    new_robot.set_facing(Direction.south)
                elif direction.lower() == "e":
                    new_robot.init_facing = Direction.east
                    new_robot.set_facing(Direction.east)
                elif direction.lower() == "w":
                    new_robot.init_facing = Direction.west
                    new_robot.set_facing(Direction.west)

                
                self.new_robot = new_robot

                #QtWidgets.QMessageBox.information(self, "Initialize robot location", f"Click on square of the game grid where Robot {name} should be placed!")
                self.adding_robot = True
                self.adding_obs = False
            else:
                self.change_bt_color_back(self.button_initbot)
        else:
            self.change_bt_color_back(self.button_initbot)
                
                

    def mousePressEvent(self, event):
        # pixel_x = event.pos().x()
        # self.clicked_x = pixel_x // self.square_size

        # pixel_y = event.pos().y()
        # self.clicked_y = pixel_y // self.square_size

        scene_pos = self.view.mapToScene(event.pos())
        # test = event.scenePos()
        test_2 = event.pos()

        print("widget_pos?viewport? event.pos(): ", test_2)
        print("event.pos() mapped to scene coordinates: ", scene_pos)
      
        pixel_x = scene_pos.x() - 182
        pixel_y = scene_pos.y() - 15
      
        self.clicked_x = int((pixel_x/self.square_size))
        self.clicked_y = int((pixel_y/self.square_size))
        
        location = Coordinates(self.clicked_x, self.clicked_y)

        print(f"Clicked on square ({self.clicked_x}, {self.clicked_y})")
        print(f"event.pos() mapped scene coordinates - 182: {pixel_x} | event.pos() mapped scene coordinates - 15: {pixel_y}")


        if self.grid_drawn:
            if pixel_x < 0 or pixel_y < 0 or pixel_x > self.square_size * self.world.width or pixel_y > self.square_size * self.world.height: 
            # if self.clicked_x not in range(0, self.world.width) or self.clicked_y not in range(0, self.world.height):
                QtWidgets.QMessageBox.warning(self, "Error", "Please click within the grid!")
            else:             
                if self.adding_obs: ###### Flag of choosing obstacle location
                        location = Coordinates(self.clicked_x, self.clicked_y)
                        clicked_square = self.world.get_square(location)
                        if not clicked_square.is_empty():
                            QtWidgets.QMessageBox.warning(self, "Error", "Please click on an empty square!")
                        else:
                            clicked_square.set_wall()
                            self.added_obs_amount += 1
                            self.draw_obs(location)
                            # self.adding_obs = False

                elif self.adding_robot:  ###### Flag of choosing robot location 
                    if self.new_robot is None:
                        QtWidgets.QMessageBox.warning(self, "Error", "Please add robot first!")
                                    
                    else:
                        location = Coordinates(self.clicked_x, self.clicked_y)                  
                        clicked_square = self.world.get_square(location)              
                        if not clicked_square.is_empty():
                            QtWidgets.QMessageBox.warning(self, "Error", "Please click on an empty square!")
                        else:
                            self.new_robot.init_location = location
                            self.new_robot.set_location(location)
                            if self.new_robot not in self.world.robots:
                                self.world.add_robot(self.new_robot, location, self.new_robot.get_facing())   
                                self.world.robots.append(self.new_robot)
                                clicked_square.set_robot(self.new_robot)                         
                                
                                self.draw_robots(self.new_robot)

                                self.change_bt_color_back(self.button_initbot)                                  
                                self.adding_robot = False            

                                    #QtWidgets.QMessageBox.information(self, "Set algorithm", f"Click on the Robot {self.new_robot.get_name()} to set an algorithm!") 

    # def setting_algorithm(self, robot):               
    #                 elif clicked_square.get_robot() is not None and clicked_square.get_robot().setting_algorithm():
                        
    #                     clicked_robot = clicked_square.get_robot()
    #                     algorithm, ok = QtWidgets.QInputDialog.getItem(self, "Set Algorithm", "Choose an algorithm:", Brain.algorithms, 0, False)
    #                     if ok:
    #                         if algorithm == "Random Path":
    #                             brain = RandomPath(clicked_robot)
    #                             clicked_robot.set_brain(brain)
                            
    #                         elif algorithm == "A* Path":
    #                             pass
    #                         elif algorithm == "Greedy Path":
    #                             pass
    #                         else:
    #                             pass
                
    def keyPressEvent(self, event):
        if self.obs_bt_clicked:
            key = event.key()
            if key == QtCore.Qt.Key.Key_W:
                self.adding_obs = True
                self.change_bt_color(self.button_initobs)

    def keyReleaseEvent(self, event):
        if self.obs_bt_clicked:
            key = event.key()
            if key == QtCore.Qt.Key.Key_W:
                self.adding_obs = False
                self.obs_bt_clicked = False
                self.change_bt_color_back(self.button_initobs)
                                     
    def draw_robots(self, robot):
        robot_gui = GuiRobot(robot, self.square_size, self)    #### making main window widget as parent of robot graphic item
        self.added_robot_gui.append(robot_gui)
        self.scene.addItem(robot_gui)

        return robot_gui
        
    
    def init_finalize_bt(self):
        self.button_finalize = QtWidgets.QPushButton('Finalize Robot World', self)

        self.button_finalize.clicked.connect(lambda: self.change_bt_color(self.button_finalize))
        self.button_finalize.clicked.connect(self.finalize_world)
      
        self.button_layout.addWidget(self.button_finalize)

    def finalize_world(self):
        if not len(self.added_robot_gui) > 0 or self.added_obs_amount < 3:  
            ## either condition is true, warning message will be displayed  
            ### if len() > 0 and added_obs_amount > 3: .....  
            ### else: error message

            QtWidgets.QMessageBox.warning(self, "Error", "Please add at least one robot and three obstacles first!")
            self.change_bt_color_back(self.button_finalize)
        else: 
            self.button_layout.removeWidget(self.button_initbot)
            self.button_initbot.deleteLater()

            self.button_layout.removeWidget(self.button_initobs)
            self.button_initobs.deleteLater()

            self.button_layout.removeWidget(self.button_finalize)
            self.button_finalize.deleteLater()
            
            self.world_finalized = True
            self.place_dirts()

    def place_dirts(self):
        if self.world_finalized:
                num_dirts = random.randint(10, 100)
                for _ in range(num_dirts):
                    while True:
                        x = random.randint(0, self.world.width - 1)
                        y = random.randint(0, self.world.height - 1)

                        square = self.world.get_square(Coordinates(x, y))
                        if square.is_empty():
                            break
                    
                    dirt = Dirt(x, y, 5)
                    square.dirts_per_square.append(dirt)
                    self.world.dirts.append(dirt)   #### logical dirt added

                    dirt.draw_dirt(self.scene, self.square_size)  #### gui dirt added
                     
    def remove_dirts(self, dirt):  #### remove gui dirt from the window/screen right away when remove_dirts() is called

        self.scene.removeItem(dirt.get_dirt_gui())

        square = self.world.get_square(dirt.get_location())   ##### removing logical dirt
        square.dirts_per_square.remove(dirt)
        self.world.dirts.remove(dirt)


    def get_gui_robots(self):
        return self.added_robot_gui
    
    def update_gui_robots(self):
        for robot_gui in self.added_robot_gui:
            robot_gui.update()





                
  





                