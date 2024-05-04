from gui_window import GuiWindow
import sys
from PyQt6 import QtWidgets
from coordinates import Coordinates
from direction import Direction


def main():
    current = Coordinates(0, 0)
    new = current.get_target_coordinates(Direction.east, 2)
    print(new)

    app = QtWidgets.QApplication(sys.argv)
    gui = GuiWindow(100)

    sys.exit(app.exec())


    
if __name__ == "__main__":
    main()