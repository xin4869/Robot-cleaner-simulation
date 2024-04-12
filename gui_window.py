from PyQt6 import QtWidgets, QtGui, QtCore

from coordinates import Coordinates
from robotworld import RobotWorld
from robot import Robot

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
        text, ok = QtWidgets.QInputDialog.getText(self, 'Add Robot to World', 'Enter robot name:')
        if ok:
            if text in [robot.get_name() for robot in self.world.robots]:
                QtWidgets.QMessageBox.warning(self, "Error", f"Robot {text} already exists in the world!")
            else:
                self.world.robots.append()





    def init_button(self):
        self.button_initbot = QtWidgets.QPushButton('Create Robot', self)
        self.button_add.clicked.connect(self.create_robot)

        

