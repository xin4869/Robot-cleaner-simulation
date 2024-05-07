from coordinates import Coordinates
import random

from PyQt6 import QtWidgets, QtGui, QtCore

class Dirt():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def get_location(self):
        return Coordinates(self.x, self.y)

    def draw_dirt(self, scene, square_size):
        x_gui = self.x * square_size + random.uniform(3, square_size - self.size)
        y_gui = self.y * square_size + random.uniform(3, square_size - self.size)

        dirt = QtWidgets.QGraphicsEllipseItem(x_gui, y_gui, self.size, self.size)
                    
        brush = QtGui.QBrush(QtCore.Qt.BrushStyle.Dense3Pattern)
        brush.setColor(QtGui.QColor(150, 75, 0))  ### Brown color brush
        dirt.setBrush(brush)

        scene.addItem(dirt)



        

