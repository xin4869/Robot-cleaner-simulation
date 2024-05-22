from PyQt6 import QtCore, QtGui, QtWidgets

class GuiSquare(QtWidgets.QGraphicsRectItem):
    def __init__(self, square, parent=None):
        super().__init__(parent)
        self.square = square
        self.setRect(0, 0, 50, 50)
        self.setBrush(QtGui.QColor(0, 0, 0))