from PyQt6 import QtWidgets, QtGui, QtCore

from coordinates import Coordinates
from robotworld import RobotWorld
from robot import Robot
from direction import Direction

class GuiWindow(QtWidgets.QMainWindow):
    def __init__(self, world, square_size):
        super().__init__()
        self.added_robot = []
        self.added_robot_gui = []
        self.world = world
        self.square_size = square_size

        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)

        clicked_x = None
        clicked_y = None


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
                world = RobotWorld(int(text.split(",")[0]), int(text.split(",")[1]))
                QtWidgets.QMessageBox.information(self, "Success", "World created successfully!")


    def create_robot(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Create Robot', 'Enter robot name:')
        if ok:
            new_robot = Robot(text)
            QtWidgets.QMessageBox.information(self, "Success", f"Robot {text} created successfully!")


    def add_to_world(self):
        name, ok = QtWidgets.QInputDialog.getText(self, 'Initialize Robot', 'Enter robot name:')
        if ok:
            if name in [robot.get_name() for robot in self.world.robots]:
                QtWidgets.QMessageBox.warning(self, "Error", f"Robot {name} already exists in the world!")
            else:
                new_robot = Robot(name)
                direction, ok = QtWidgets.QInputDialog.getText(self, "Initialize robot direction", f"Which direction should Robot {name} face? Enter one of these: N, S, E, W")
                ### message box close by itself?
                if ok:
                    if direction.lower*() == "n":
                        new_robot.set_facing(Direction.north)
                    elif direction.lower() == "s":
                        new_robot.set_facing(Direction.south)
                    elif direction.lower() == "e":
                        new_robot.set_facing(Direction.east)
                    elif direction.lower() == "w":
                        new_robot.set_facing(Direction.west)
                    else:
                        QtWidgets.QMessageBox.warning(self, "Error", "Invalid direction! Robot not initialized.")
                    QtWidgets.QMessageBox.information(self, "Initialize robot location", f"Click on square of the game grid where Robot {name} should be placed!")

                    if self.clicked_x or self.clicked_y == None:
                        QtWidgets.QMessageBox.warning(self, "Error", "Please click on square of the game grid where Robot {name} should be placed!")
                    else:
                        location = Coordinates(self.clicked_x, self.clicked_y)
                        self.world.set_robot(new_robot, location, new_robot.get_facing())    

    
    def mousePressEvent(self, event):
        self.clicked_x = event.x()
        self.clicked_y = event.y()
     

    def init_button(self):
        self.button_initbot = QtWidgets.QPushButton('Create Robot', self)
        self.button_add.clicked.connect(self.create_robot)

        

