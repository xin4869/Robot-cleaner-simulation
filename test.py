import unittest
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6 import QtTest
from gui_window import GuiWindow
from gui_robot import GuiRobot

from coordinates import Coordinates
from robotworld import RobotWorld
from robot import Robot
from direction import Direction
from square import Square
from dirt import Dirt
from brain import Brain
from random_mode import RandomMode
from rules import Rules
from setting import Setting

class Test(unittest.TestCase):
    def setUp(self):
        self.app = QtWidgets.QApplication([])

    def tearDown(self):
        self.app.quit()

    def test_window_setup(self):
        window = GuiWindow(100)
        self.assertEqual(window.square_size, 100)
        
        button = window.findChild(QtWidgets.QPushButton, 'Initialize grid')
        self.assertIsNotNone(button)

    def test_initalize_grid(self):
        window = GuiWindow(100)
        button = window.findChild(QtWidgets.QPushButton, 'Initialize grid')
        self.assertIsNotNone(button)

        button.click()
        self.assertEqual(window.world.width, 10)
        self.assertEqual(window.world.height, 8)
        self.assertEqual(window.grid_drawn, True)
        self.assertTrue(window.world)

