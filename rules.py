from PyQt6 import QtWidgets, QtCore, QtGui


class Rules(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Robot World Rules")
        self.setFixedSize(600, 1000)
        rule = QtWidgets.QTextEdit(self)

       
        text = (    "<h1 style='text-align:center;'>Robot World Rules</h1>"
                    "<p style='font-size:16pt;'>1. Click the button <u>Initialize grid</u>.<br>"
                    "Note: Default window size is 10 x 8, but you may adjust the window size<br>according to the grid size.<br><br>"
                    "2.  Click on buttons <u>Place obstacle</u>, <u>Add Robot</u> to set walls and robots.<br>"
                    "Note: You need to add at least 1 robot, 3 obstacles and set an algorithm for each robot to finalize the set up.<br><br>"                   
                    "3.  Click the button <u>Finalize Robot World</u> to finish the set up.<br>"
                    "Note: Once you have finalized the set up, you cannot make changes. However, you can always change algorithms.<br><br>"
                    "4.  Click on the robot to switch vaccum power (Standard or Strong). <br>"
                    "Note: In Strong vacuum power mode, robots will clean more efficiently, but their battery consumption will be higher.<br><br>"
                    "5. If the robot is destroyed(red), you may click on the robot to reset it.<br>"
                    "Note: A stuck robot will be destroyed after 6 failed attempts to move.<p>"
                    
                     "<h2 style = 'text-align:center;'>Add robot</h2>"
                    "<p style = 'font-size:16pt;'>1. Click the button <u>Add Robot</u>.<br><br>"
                    "2. Click on the squares in which you want to place the robot.<br><br>"
                    "3. Click on robots to set algorithms. <br><br>"
                    "Note: You may click on robots to reset algorithms later.<p>"

                    "<h2 style = 'text-align:center;'>Add obstacles</h2>"
                    "<p style = 'font-size:16pt;'>1. Click the button <u>Place obstacle</u>.<br><br>"
                    "2. Hold the key W while clicking on squares to place obstacles. <br>"
                    "Note: Release the key W only when you finish adding all obstacles.<br>"
                    "Note: You may not remove added obstacles.<p> "

                    "<h2 style='text-align:center;'>Robot colors</h2>"
                    "<p style = 'font-size:16pt;'> 1. <strong>Gray</strong>: No algorithm has been set.<br><br>"
                    " 2. <strong>Purple</strong> : All good.<br><br>"
                    " 3. <strong>Yellow</strong> : Stuck.<br><br>"
                    " 4. <strong>Pink</strong> : Battery low.<br><br>"
                    " 5. <strong>Red</strong>: Destroyed.<p>"

                    "<h2 style = 'text-align:center;'>Algorithms</h2>"
                    "<p style = 'font-size:16pt;'>1. <strong>Random Mode</strong>: The robot moves in random direction.<br><br>"
                    "2. <strong>Standard Mode</strong>: The robot try to cover the whole room efficiently by reducing repeatitive movements.<br><br>"
                    "3. <strong>Dirt Prioritizer Mode</strong>: The robot will move on only when all dirt at current spot is removed, while trying to cover the whole room efficiently by reducing repeatitive movements.<br><br>"
                    "4. <strong>Recharging</strong>: Every move will consume 1-2 battery depending on vacuum power. When the battery level is lower than 1/4, the robot will find its way back to initial location to recharge. <p>")
        
        rule.setReadOnly(True)
        rule.setFontFamily("Arial")
        rule.setHtml(text)
        # rule.setText(text)
        rule.setFixedSize(600, 1000)
        # rule.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # document = rule.document()
        # document.setDefaultTextOption(QtGui.QTextOption(QtCore.Qt.AlignmentFlag.AlignCenter))
        