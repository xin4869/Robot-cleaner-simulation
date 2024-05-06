from PyQt6 import QtWidgets, QtGui, QtCore

from coordinates import Coordinates
from robotworld import RobotWorld
from robot import Robot
from direction import Direction
from square import Square

from gui_robot import GuiRobot

class GuiWindow(QtWidgets.QMainWindow):
    def __init__(self, square_size):
        super().__init__()
        self.added_robot = []
        self.added_robot_gui = []
        self.world = None
        self.square_size = square_size

        self.setCentralWidget(QtWidgets.QWidget())
        self.main_layout = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.main_layout)

        self.init_world_bt()
        self.button_layout = QtWidgets.QVBoxLayout()
        self.button_layout.addWidget(self.button_initworld)
        
        self.main_layout.addLayout(self.button_layout)

        self.grid_drawn = False
        self.adding_robot = False
        self.adding_wall = False

        self.clicked_x = None
        self.clicked_y = None

        self.new_robot = None

        self.init_window()
        

    def init_window(self):
        self.setGeometry(1000, 500, 1200, 850)
        self.setWindowTitle('Robot World')
        self.show()

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1000, 900)

        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.main_layout.addWidget(self.view)


    def init_world_bt(self):
        self.button_initworld = QtWidgets.QPushButton('Initialize grid', self)
        self.button_initworld.clicked.connect(self.create_world)
        

    def create_world(self):
        text,ok = QtWidgets.QInputDialog.getMultiLineText(self, 'Create Robot World', 'Enter world width dimension, eg.10:')
        if ok:
            if text == "":
                QtWidgets.QMessageBox.warning(self, "Error", "Please enter width dimensions!")
            elif text.isdigit() == False: 
                QtWidgets.QMessageBox.warning(self, "Error", "Please enter only numeric values!")
            else:
                width = int(text)
                text,ok = QtWidgets.QInputDialog.getMultiLineText(self, 'Create Robot World', 'Enter world height dimension, eg.8:')
                if ok:
                    if text == "":
                        QtWidgets.QMessageBox.warning(self, "Error", "Please enter height dimensions!")
                    elif text.isdigit() == False: 
                        QtWidgets.QMessageBox.warning(self, "Error", "Please enter only numeric values!")
                    else:
                        height = int(text)
                        self.world = RobotWorld(width, height)
                        #QtWidgets.QMessageBox.information(self, "Success", "Robot World initialized successfully!")
                        # msg_box = QtWidgets.QMessageBox()
                        # msg_box.setText("Robot World initialized successfully!")
                        # msg_box.exec()
                        self.draw_grid()
                        self.grid_drawn = True
                        
                        self.init_bot_bt()
                        self.button_layout.removeWidget(self.button_initworld)
                        self.button_initworld.deleteLater()


    def draw_grid(self):
        for y in range(self.world.get_height()):
            for x in range(self.world.get_width()):              
                x_gui = x * self.square_size
                y_gui = y * self.square_size
                square_gui = QtWidgets.QGraphicsRectItem(x_gui, y_gui, self.square_size, self.square_size)

                square = self.world.get_square(Coordinates(x, y))
                if square.is_wall():
                    square_gui.setBrush(QtGui.QColor(128, 128, 128))
                else:
                    square_gui.setBrush(QtGui.QColor(255, 255, 255))

                self.scene.addItem(square_gui)


    def init_bot_bt(self):
        if self.grid_drawn:
            self.button_initbot = QtWidgets.QPushButton('Add Robot', self)
            self.button_initbot.clicked.connect(self.add_to_world)
            self.button_layout.addWidget(self.button_initbot)


    def add_to_world(self):
        
        name, ok = QtWidgets.QInputDialog.getText(self, 'Initialize Robot', 'Enter robot name:')
        if ok:
            while name in [robot.get_name() for robot in self.world.robots]:
                response = QtWidgets.QMessageBox.warning(self, "Error", f"Robot {name} already exists in the world!", QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)
                
                if response == QtWidgets.QMessageBox.Cancel:
                    return
                
                name, ok = QtWidgets.QInputDialog.getText(self, 'Initialize Robot', 'Enter robot name:')
                if not ok:
                    return
        
            new_robot = Robot(name)      

            direction, ok = QtWidgets.QInputDialog.getText(self, "Initialize robot direction", f"Which direction should Robot {name} face? Enter one of these: N, S, E, W (North, South, East, West).")       
            if ok:
                while direction.lower() not in ["n", "s", "e", "w"]:
                    response = QtWidgets.QMessageBox.warning(self, "Error", "Invalid direction! Please enter a valid direction.", QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)

                    if response == QtWidgets.QMessageBox.Cancel:
                        return
                    
                    direction, ok = QtWidgets.QInputDialog.getText(self, "Initialize robot direction", f"Which direction should Robot {name} face? Enter one of these: N, S, E, W")
                    
                    if not ok:
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

                QtWidgets.QMessageBox.information(self, "Initialize robot location", f"Click on square of the game grid where Robot {name} should be placed!")
                self.adding_robot = True
                
                

    def mousePressEvent(self, event):
        # pixel_x = event.pos().x()
        # self.clicked_x = pixel_x // self.square_size

        # pixel_y = event.pos().y()
        # self.clicked_y = pixel_y // self.square_size

        scene_pos = self.view.mapToScene(event.pos())
        pixel_x = scene_pos.x() - 123
        pixel_y = scene_pos.y() - 15
        self.clicked_x = int((pixel_x/self.square_size))
        self.clicked_y = int((pixel_y/self.square_size))


        print(f"Clicked on square ({self.clicked_x}, {self.clicked_y})")
        print(f"pixel_x: {pixel_x} | pixel_y: {pixel_y}")

        if self.grid_drawn:
            if pixel_x < 0 or pixel_y < 0 or pixel_x > self.square_size * self.world.width or pixel_y > self.square_size * self.world.height: 
            # if self.clicked_x not in range(0, self.world.width) or self.clicked_y not in range(0, self.world.height):
                QtWidgets.QMessageBox.warning(self, "Error", "Please click within the grid!")
            else:
                if self.new_robot is None:
                    QtWidgets.QMessageBox.warning(self, "Error", "Please add robot first!")
                    print(self.added_robot) ########### TO BE DELETED
                else:
                    if self.world is None:
                        QtWidgets.QMessageBox.warning(self, "Error", "Please initialize Robot World first!")
                    else:
                        if self.adding_robot:  ###### Flag of choosing robot location               
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
                                    self.added_robot.append(self.new_robot)  
                                    clicked_square.set_robot(self.new_robot)                         
                                    QtWidgets.QMessageBox.information(self, "Success", f"Robot {self.new_robot.get_name()} has been initialized successfully!")

                                    print(self.added_robot) ################ TO BE DELETED
                                    
                                    self.adding_robot = False

                                    self.draw_robots()
                                else:
                                    QtWidgets.QMessageBox.warning(self, "Error", f"Robot {self.new_robot.get_name()} already exists in the world! Please click Add Robot to add another robot!")
                        

      
    def draw_robots(self):
        for robot in self.world.robots:
            robot_gui = GuiRobot(robot, self.square_size)
            self.added_robot_gui.append(robot_gui)
            self.scene.addItem(robot_gui)
        

 



                
  





                