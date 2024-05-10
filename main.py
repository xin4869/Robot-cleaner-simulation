from gui_window import GuiWindow
import sys
from PyQt6 import QtWidgets
from coordinates import Coordinates
from direction import Direction


def main():
 
    app = QtWidgets.QApplication(sys.argv)
    window1 = GuiWindow(100)

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()