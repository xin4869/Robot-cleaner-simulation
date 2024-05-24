import unittest
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6 import QtTest
from gui_window import GuiWindow
from gui_robot import GuiRobot
from gui_square import GuiSquare

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

import sys
from unittest.mock import patch

class Test(unittest.TestCase): 

    def setUp(self):    
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = GuiWindow(100)
        self.window.show()

    def tearDown(self):
        self.app.exit()
        self.window.close()
        
    def test_app_setup(self):
        self.assertIsNotNone(self.app)
    
    def test_gui_window_setup(self):
        self.assertIsNotNone(self.window)

    def test_window_setup(self):
        self.assertEqual(self.window.square_size, 100)

    def test_layout_setup(self):
        self.assertIsNotNone(self.window.main_layout)
        self.assertIsNotNone(self.window.button_layout)
    
    def test_rules_bt(self):  
        self.assertIsNotNone(self.window.button_rules)
        self.assertIsNotNone(self.window.button_initworld)

    @patch('PyQt6.QtWidgets.QInputDialog.getMultiLineText')
    def test_create_world(self, mock_input_dialog):
        mock_input_dialog.side_effect = [("10", True), ("8", True)]

        button = self.window.button_initworld
        button.click()

        self.assertEqual(self.window.world.width, 10)
        self.assertEqual(self.window.world.height, 8)
        self.assertTrue(self.window.grid_drawn)
        self.assertTrue(self.window.world)
    
    def test_bot_obs_bt(self):
        self.test_create_world()
        self.assertIsNotNone(self.window.button_initbot)
        self.assertIsNotNone(self.window.button_initobs)


    @patch('PyQt6.QtWidgets.QInputDialog.getText')
    def test_add_to_world(self, mock_input_dialog):
        self.test_bot_obs_bt()

        mock_input_dialog.side_effect = [("little white", True), ("n", True)]

        button = self.window.button_initbot
        button.click()

        self.assertIsNotNone(self.window.new_robot)
        self.assertTrue(self.window.adding_robot)
        self.assertFalse(self.window.adding_obs)
    

    def test_robot_location(self):
        self.test_add_to_world()

        scene_pos = QtCore.QPointF(3 * self.window.square_size + self.window.square_size / 2, 4 * self.window.square_size + self.window.square_size / 2)

        clicked_view_pos = self.window.view.mapFromScene(scene_pos)
        self.assertIsNotNone(clicked_view_pos)
        self.assertIsNotNone(self.window.view.viewport())
    
        QtTest.QTest.mousePress(self.window.view.viewport(), QtCore.Qt.MouseButton.LeftButton, QtCore.Qt.KeyboardModifier.NoModifier,clicked_view_pos)
        
        clicked_item = self.window.scene.itemAt(scene_pos, self.window.view.transform())
        self.assertIsInstance(clicked_item, GuiRobot)


    # def test_setting_algorithm(self):
    #     self.test_robot_location()
        


if __name__ == "__main__":
    unittest.main()