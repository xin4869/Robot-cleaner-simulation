from PyQt6 import QtWidgets, QtCore, QtGui


class Rules(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Robot World Rules")
        self.setFixedSize(600, 800)
        rule = QtWidgets.QTextEdit(self)

       
        text = (    "<h1 style='text-align:center;'>Robot World Rules</h1>"
                    "<p style='font-size:16pt;'>1. Click the button Initialize grid.<br><br>"
                    "2.  Click on buttons <Place obstacles> or <Add Robot> to add walls or robots.<br>"
                    "NB: You need to add at least 1 robot and 3 obstacles.<br><br>"
                    "3. Click on robots to add algorithms to run. <br> "
                    "NB: You may click on robots to reset algorithms later.<br><br> "
                    "4.  Click the button <Finalize World> to finish the set up.<br>"
                    "NB: Once you have finalized the set up, you cannot make changes.<br><br>"
                    "5. If the robot turns red(broken), you may click on it for reseting.<p>"
                    "<h2 style='text-align:center;'>Robot colors</h2>"
                    "<p style = 'font-size:16pt;'> 1. Yello robots(incomplete): <br> no algorithm has been set.<br><br>"
                    " 2. Red robots (broken): <br> the robot has been destroyed.<br><br>"
                    " 3. Purple robots: <br> functioning robots.<p>"
                    "<h2 style = 'text-align:center;'>Algorithms</h2>"
                    "<p style = 'font-size:16pt;'>1. Random Path:<br> The robot moves randomly.<br><br>"
                    "2. A * Path: <br> The robot moves according to the A* algorithm.<p>")
        
        rule.setReadOnly(True)
        rule.setFontFamily("Arial")
        rule.setHtml(text)
        # rule.setText(text)
        rule.setFixedSize(600, 800)
        # rule.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        document = rule.document()
        document.setDefaultTextOption(QtGui.QTextOption(QtCore.Qt.AlignmentFlag.AlignCenter))
        