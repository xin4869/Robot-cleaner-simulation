from PyQt6 import QtWidgets, QtGui, QtCore

from coordinates import Coordinates

class GuiWindow(QtWidgets.QMainWindow):
    def __init__(self, world, square_size):
        super().__init__()
        