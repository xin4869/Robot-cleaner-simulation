from PyQt6 import QtWidgets, QtGui, QtCore
from direction import Direction
from brain import Brain
from random_path import RandomPath

class GuiRobot(QtWidgets.QGraphicsPolygonItem):
    algorithms = ["Random Path", "A* Path", "Greedy Path"]
    vacuum_power = ["Standard", "Strong"]
    def __init__(self, robot, square_size, parent=None):
        super().__init__()
        self.robot = robot
        self.square_size = square_size
        self.parent = parent

        self.triangle()
        self.update()
        
        # brush = QtGui.QBrush(QtCore.Qt.BrushStyle.SolidPattern)
        # self.setBrush(brush)


    def triangle(self):
        triangle = QtGui.QPolygonF()
        triangle.append(QtCore.QPointF(self.square_size/2, 0))
        triangle.append(QtCore.QPointF(0, self.square_size))
        triangle.append(QtCore.QPointF(self.square_size, self.square_size))
        triangle.append(QtCore.QPointF(self.square_size/2, 0))

        self.setPolygon(triangle)
        self.setTransformOriginPoint(self.square_size/2, self.square_size/2)

    def updatePos(self):
        x_gui= self.square_size * self.robot.get_location().get_x()
        y_gui = self.square_size * self.robot.get_location().get_y()
        self.setPos(x_gui, y_gui)

    def rotate(self):
        facing = self.robot.get_facing()
        degree = {Direction.north: 0, Direction.east: 90, Direction.south: 180, Direction.west: 270}
        
        self.setRotation(degree[facing])

    def color(self):
        brush = QtGui.QBrush()

        if self.robot.destroyed:
            brush.setStyle(QtCore.Qt.BrushStyle.CrossPattern)
            brush.setColor(QtGui.QColor(255, 0, 0))
        elif 0 < self.robot.battery <= 100:
            brush.setStyle(QtCore.Qt.BrushStyle.CrossPattern)
            brush.setColor(QtGui.QColor(255, 150, 150))
        elif self.robot.is_really_stuck:
            brush.setStyle(QtCore.Qt.BrushStyle.CrossPattern)
            brush.setColor(QtGui.QColor(255, 221, 51))
        elif self.robot.is_incomplete():
            brush.setStyle(QtCore.Qt.BrushStyle.DiagCrossPattern)
            brush.setColor(QtGui.QColor(128, 128, 128))
        else:
            brush.setStyle(QtCore.Qt.BrushStyle.Dense4Pattern)
            brush.setColor(QtGui.QColor(180, 160, 210))

        self.setBrush(brush)

    def update(self):
        self.updatePos()
        self.rotate()
        self.color()

    
    def setting_algorithm(self, algorithm):
        if algorithm == "Random Path":
            brain = RandomPath(self.robot)
            self.robot.set_brain(brain)
                   
        elif algorithm == "A* Path":
            pass
        elif algorithm == "Greedy Path":
            pass
        else:
            pass


    def setting_vacuum_power(self, vacuum_power):
        if vacuum_power == "Standard":
            self.robot.mode = 0
        elif vacuum_power == "Strong":
            self.robot.mode = 1
    
    def mousePressEvent(self, event):
        if self.robot.destroyed and not self.robot.is_incomplete():
            self.robot.reset()
            event.accept()

        else:
            # print("item coordinates: ",event.pos())
            clicked_point = event.scenePos()
            # print("scene coordinates: ", clicked_point)
            scene = self.parent.get_scene()
            item = scene.itemAt(clicked_point, QtGui.QTransform())
            # print("clicked item type: ", type(item))

            
            if item == self:
                menu = QtWidgets.QMenu(self.parent)
                menu_vaccum = QtWidgets.QMenu("Vaccum Power", self.parent)
                menu_algorithm = QtWidgets.QMenu("Algorithm", self.parent)
                menu.addMenu(menu_vaccum)
                menu.addMenu(menu_algorithm)

                for vacuum_power in self.vacuum_power:
                    action = QtGui.QAction(vacuum_power, self.parent)
                    action.triggered.connect(lambda checked, x = vacuum_power: self.setting_vacuum_power(x))
                    menu_vaccum.addAction(action)


                for algorithm in self.algorithms:
                    action = QtGui.QAction(algorithm, self.parent)
                    action.triggered.connect(lambda checked, x = algorithm: self.setting_algorithm(x))
                    menu_algorithm.addAction(action)

            
                menu.exec(event.screenPos())
                # menu_algorithm.exec(event.screenPos())
                # menu_vaccum.exec(event.screenPos())
