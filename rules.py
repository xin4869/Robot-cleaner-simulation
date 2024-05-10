from PyQt6 import QtWidgets, QtCore, QtGui


class Rules(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Robot World Rules")
        self.setFixedSize(600, 900)
        rule = QtWidgets.QTextEdit(self)

       
        text = (    "<h1 style='text-align:center;'>Robot World Rules</h1>"
                    "<p style='font-size:16pt;'>1. Click the button <u>Initialize grid</u>.<br><br>"
                    "2.  Click on buttons <u>Place obstacle</u>, <u>Add Robot</u> to set walls and robots.<br>"
                    "Note: You need to add at least 1 robot and 3 obstacles to finalize the world.<br><br>"                   
                    "3.  Click the button <u>Finalize Robot World</u> to finish the set up.<br>"
                    "Note: Once you have finalized the set up, you cannot make changes.<br><br>"
                    "4. If the robot is destroyed(red), you may click on the robot to reset it.<br>"
                    "Note: A stuck robot will be destroyed after 8 failed attempts to move.<p>"
                    

                     "<h2 style = 'text-align:center;'>Add robot</h2>"
                    "<p style = 'font-size:16pt;'>1. Click the button <u>Add Robot</u>.<br>"
                    "2. Click on the squares in which you want to place the robot.<br>"
                    "3. Click on robots to set algorithms. <br> "
                    "Note: You may click on robots to reset algorithms later.<p>"

                    "<h2 style = 'text-align:center;'>Add obstacles</h2>"
                    "<p style = 'font-size:16pt;'>1. Click the button <u>Place obstacle</u>.<br><br>"
                    "2. Hold down the key W. <br><br>"
                    "3. Click on the squares in which you want to place the obstacle.<br>"
                    "Note: You may not remove added obstacles.<br><br>"
                    "4. Release the key only when you finish adding all obstacles. <p> "

                    "<h2 style='text-align:center;'>Robot colors</h2>"
                    "<p style = 'font-size:16pt;'> 1. <strong>Gray</strong>: No algorithm has been set.<br><br>"
                    " 2. <strong>Purple</strong> : All good.<br><br>"
                    " 3. <strong>Yellow</strong> : Stuck.<br><br>"
                    " 4. <strong>Red</strong>: Destroyed.<p>"

                    "<h2 style = 'text-align:center;'>Algorithms</h2>"
                    "<p style = 'font-size:16pt;'>1. <strong>Random Path</strong>: The robot moves in random direction.<br><br>"
                    "2. <strong>A * Path</strong>: The robot moves according to the A* algorithm.<p>")
        
        rule.setReadOnly(True)
        rule.setFontFamily("Arial")
        rule.setHtml(text)
        # rule.setText(text)
        rule.setFixedSize(600, 900)
        # rule.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # document = rule.document()
        # document.setDefaultTextOption(QtGui.QTextOption(QtCore.Qt.AlignmentFlag.AlignCenter))
        