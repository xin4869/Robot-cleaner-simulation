from PyQt6 import QtCore, QtGui, QtWidgets

class GuiSquare(QtWidgets.QGraphicsRectItem):
    def __init__(self, square, square_size, parent=None):
        super().__init__()
        self.parent = parent
        self.square = square
        self.x = square.x * square_size
        self.y = square.y * square_size
        self.setRect(self.x, self.y, square_size, square_size)
        self.square.set_gui(self)
        
        # self.brush = QtGui.QBrush()
        # self.brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        # self.brush.setColor(QtGui.QColor(255, 255, 255))
        # self.setBrush(self.brush)

        self.setBrush(QtGui.QColor(255, 255, 255))


    def mousePressEvent(self, event):
        clicked_point = event.scenePos()
        scene = self.parent.get_scene()
        item = scene.itemAt(clicked_point, QtGui.QTransform())

        if item == self:
            if self.parent.grid_drawn:
                if self.parent.adding_obs:
                    if self.square.is_empty():
                        self.square.set_wall()
                        self.parent.added_obs_amount += 1

                        brush = self.brush()
                        brush.setColor(QtGui.QColor(200, 200, 200))
                        brush.setStyle(QtCore.Qt.BrushStyle.CrossPattern)
                        self.setBrush(brush)
                    else:
                        QtWidgets.QMessageBox.warning(self.parent, "Warning", "Square is not empty!")

                elif self.parent.adding_robot:
                    if self.parent.new_robot is None:
                        QtWidgets.QMessageBox.warning(self.parent, "Warning", "Please add Robot first!")
                    else:
                        if self.square.is_empty():
                            self.parent.new_robot.init_location = self.square.get_location()
                            self.parent.new_robot.set_location(self.square.get_location())
                            self.parent.new_robot.set_inner_location(self.parent.new_robot.init_inner_location)

                            self.square.set_robot(self.parent.new_robot)
                            self.parent.new_robot.set_world(self.parent.world)
                            
                            self.parent.draw_robots(self.parent.new_robot)                            
                            self.parent.change_bt_color_back(self.parent.button_initbot)

                            if self.parent.new_robot not in self.parent.world.robots:                   
                                self.parent.world.robots.append(self.parent.new_robot)
                            
                            self.parent.adding_robot = False
                                
                        else:
                            QtWidgets.QMessageBox.warning(self.parent, "Warning", "Square is not empty!")