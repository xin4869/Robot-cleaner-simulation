from PyQt6 import QtWidgets, QtGui, QtCore

from coordinates import Coordinates
from robotworld import RobotWorld
from robot import Robot
from direction import Direction

class GuiWindow(QtWidgets.QMainWindow):
    def __init__(self, square_size):
        super().__init__()
        self.added_robot = []
        self.added_robot_gui = []
        self.world = None
        self.square_size = square_size

        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)

        self.clicked_x = None
        self.clicked_y = None

        self.new_robot = None


    def init_window(self):
        self.setGeometry(1300, 500, 800, 800)
        self.setWindowTitle('Robot World')
        self.show()

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 700)

        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)

    def create_world(self):
        text,ok = QtWidgets.QInputDialog.getMultiLineText(self, 'Create Robot World', 'Enter world dimensions(width, height):')
        if ok:
            if text == "":
                QtWidgets.QMessageBox.warning(self, "Error", "Please enter world dimensions")
            elif len(text) != 2:
                QtWidgets.QMessageBox.warning(self, "Error", "Please enter both dimensions in order: width, height!")
            else:
                self.world = RobotWorld(int(text.split(",")[0]), int(text.split(",")[1]))
                QtWidgets.QMessageBox.information(self, "Success", "Robot World initialized successfully!")


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
                    new_robot.set_facing(Direction.north)
                elif direction.lower() == "s":
                    new_robot.set_facing(Direction.south)
                elif direction.lower() == "e":
                    new_robot.set_facing(Direction.east)
                elif direction.lower() == "w":
                    new_robot.set_facing(Direction.west)

                
                self.new_robot = new_robot

                QtWidgets.QMessageBox.information(self, "Initialize robot location", f"Click on square of the game grid where Robot {name} should be placed!")


    def mousePressEvent(self, event):

        pixel_x = event.x()
        self.clicked_x = pixel_x // self.square_size

        pixel_y = event.y()
        self.clicked_y = pixel_y // self.square_size

        if self.clicked_x not in range(0, self.world.width) or self.clicked_y not in range(0, self.world.height):
            QtWidgets.QMessageBox.warning(self, "Error", "Please click within the grid!")
        else:
            if self.new_robot is None:
                QtWidgets.QMessageBox.warning(self, "Error", "Please add robot before setting location!")
            else:
                if self.world is None:
                    QtWidgets.QMessageBox.warning(self, "Error", "Please initialize Robot World first!")
                else:                 
                    location = Coordinates(self.clicked_x, self.clicked_y)
                    clicked_square =self.world.get_square(location)
                    if not clicked_square.is_empty:
                        QtWidgets.QMessageBox.warning(self, "Error", "Please click on an empty square!")
                    else:
                        self.new_robot.set_location(location)
                        if self.new_robot not in self.world.robots:
                            self.world.set_robot(self.new_robot, location, self.new_robot.get_facing())                      
                            self.world.robots.append(self.new_robot)
                            self.added_robot.append(self.new_robot)
                            QtWidgets.QMessageBox.information(self, "Success", f"Robot {self.new_robot.get_name()} has been initialized successfully!")
                        else:
                            QtWidgets.QMessageBox.warning(self, "Error", f"Robot {self.new_robot.get_name()} already exists in the world!")
                

    def init_button(self):
        self.button_initworld = QtWidgets.QPushButton('Initialize grid', self)
        self.button_initworld.clicked.connect(self.create_world)
        self.horizontal.addWidget(self.button_initworld)

        self.button_initbot = QtWidgets.QPushButton('Add Robot', self)
        self.button_initbot.clicked.connect(self.add_to_world)
        self.horizontal.addWidget(self.button_initbot)

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
    
    def draw_robots(self):





                