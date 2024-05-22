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

    @classmethod
    def setUpClass(cls):
        cls.app = QtWidgets.QApplication([])

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

    def setUp(self):
        self.window = GuiWindow(100)

    def tearDown(self):
        self.window.close()

    def test_window_setup(self):
        self.assertEqual(self.window.square_size, 100)
    
    def test_rules_bt(self):  
        button = self.window.findChild(QtWidgets.QPushButton, 'button_rules')
        self.assertIsNotNone(button)

    def test_initalize_grid_bt(self):
        button = self.window.findChild(QtWidgets.QPushButton, 'button_initworld')
        self.assertIsNotNone(button)

        # button.click()
        QtTest.QTest.mouseClick(button)

        self.assertEqual(self.window.world.width, 10)
        self.assertEqual(self.window.world.height, 8)
        self.assertTrue(self.window.grid_drawn)
        self.assertTrue(self.window.world)

if __name__ == "__main__":
    unittest.main()