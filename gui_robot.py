from PyQt6 import QtWidgets, QtGui, QtCore
from direction import Direction

class GuiRobot(QtWidgets.QGraphicsPolygonItem):
    def __init__(self, robot, square_size):
        super().__init__()
        self.robot = robot
        self.square_size = square_size
        self.triangle()
        self.update()
        
        brush = QtGui.QBrush(QtCore.Qt.BrushStyle.SolidPattern)
        self.setBrush(brush)


    def triangle(self):
        triangle = QtGui.QPolygonF()
        triangle.append(QtCore.QPointF(self.square_size/2, 0))
        triangle.append(QtCore.QPointF(0, self.square_size))
        triangle.append(QtCore.QPointF(self.square_size, self.square_size))
        triangle.append(QtCore.QPointF(self.square_size/2, 0))

        self.setPolygon(triangle)
        self.setTransformOriginPoint(self.square_size/2, self.square_size/2)

    def update(self):
        self.updatePos()
        self.rotate()
        self.color()

    def updatePos(self):
        x_gui= self.square_size * self.robot.get_location().get_x()
        y_gui = self.square_size * self.robot.get_location().get_y()
        self.setPos(x_gui, y_gui)

    def rotate(self):
        facing = self.robot.get_facing()
        degree = {Direction.NORTH: 0, Direction.EAST: 90, Direction.SOUTH: 180, Direction.WEST: 270}
        
        self.setRotation(degree[facing])

    def color(self):
        brush = QtGui.QBrush(QtCore.Qt.BrushStyle.BDiagPattern)

        if self.robot.is_broken():
            brush.setColor(QtGui.QColor(255, 0, 0))
        elif self.robot.is_stuck():
            brush.setColor(QtGui.QColor(255, 255, 0))
        else:
            brush.setColor(QtGui.QColor(0, 0, 255))

        self.setBrush(brush)

    def mousePressEvent(self, event):
        if self.robot.destroyed:
            self.robot.fix()
            event.accept()





