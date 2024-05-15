from PyQt6 import QtWidgets


class Setting(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__()

        self.parent = parent
        self.setWindowTitle("Set up your cleaning!")
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
          
        room_coverage = QtWidgets.QLabel("What is the esmitated percentage, of the area to be cleaned, out of the total room area? (1-100) ")
        self.layout.addWidget(room_coverage)
        self.room_coverage_input = QtWidgets.QSpinBox()
        self.room_coverage_input.setRange(1, 100)
        self.room_coverage_input.setSuffix("%")
        self.room_coverage_input.setSingleStep(5)
        self.room_coverage_input.setValue(50)
        self.layout.addWidget(self.room_coverage_input)



        clean_level = QtWidgets.QLabel("Select cleaning mode:")
        self.layout.addWidget(clean_level)
        self.clean_level_fast = QtWidgets.QRadioButton("Fast clean")
        self.clean_level_deep = QtWidgets.QRadioButton("Deep clean")
        self.clean_level_fast.setChecked(True)

        clean_level_group = QtWidgets.QButtonGroup(self)
        clean_level_group.addButton(self.clean_level_fast)
        clean_level_group.addButton(self.clean_level_deep)

        self.layout.addWidget(self.clean_level_fast)
        self.layout.addWidget(self.clean_level_deep)


        # vaccum_power = QtWidgets.QLabel("Select vaccum power:")
        # self.layout.addWidget(vaccum_power)
        # vaccum_power_standard = QtWidgets.QRadioButton("Standard")
        # vaccum_power_strong = QtWidgets.QRadioButton("Strong")
        # vaccum_power_standard.setChecked(True)

        # vaccum_power_group = QtWidgets.QButtonGroup(self)
        # vaccum_power_group.addButton(vaccum_power_standard)
        # vaccum_power_group.addButton(vaccum_power_strong)

        # self.layout.addWidget(vaccum_power_standard)
        # self.layout.addWidget(vaccum_power_strong)



        # self.button_layout = QtWidgets.QHBoxLayout()

        # self.button1 = QtWidgets.QPushButton("Ok")
        # self.button1.clicked.connect(self.get_values)

        # self.button2 = QtWidgets.QPushButton("Cancel")
        # self.button2.clicked.connect(lambda:None)
        
        # self.button_layout.addWidget(self.button1)
        # self.button_layout.addWidget(self.button2)
        # self.layout.addLayout(self.button_layout)

        self.buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        
        self.buttons.accepted.connect(self.get_values)
        self.buttons.accepted.connect(lambda: self.parent.change_bt_color_back(self.parent.button_setting))
        self.buttons.accepted.connect(self.accept)
        

        self.buttons.rejected.connect(self.reject)
        self.buttons.rejected.connect(lambda: self.parent.change_bt_color_back(self.parent.button_setting))
        
        self.layout.addWidget(self.buttons)

        self.exec()

        
    def get_values(self):
        
        room_coverage = self.room_coverage_input.value() / 100
        clean_level = 0.7 if self.clean_level_fast.isChecked() else 0.9
        # vaccum_power = 0 if self.vaccum_power_standard.isChecked() else 1

        self.parent.world.room_coverage_taget = room_coverage
        self.parent.world.clean_level_target = clean_level






     
    