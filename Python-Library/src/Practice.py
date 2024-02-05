import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton, QMessageBox, QLineEdit, QComboBox, QRadioButton, QSlider,QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(200, 100, 500, 300)

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setSpacing(0)

        self.label1 = QLabel("Hello Core2Web")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setFixedSize(500, 30)
        self.mainLayout.addWidget(self.label1, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        self.addButton()
        self.addButton1()
        self.addButton2()
        self.init_ui()
        self.radioUI()
        self.slider()

        self.setLayout(self.mainLayout)

    def addButton(self):
        self.Button1 = QPushButton("Text Change")
        self.Button1.clicked.connect(lambda: self.label1.setText("Hello Core2Web" if self.label1.text() == "I am Here" else "I am Here"))
        self.mainLayout.addWidget(self.Button1, alignment=Qt.AlignmentFlag.AlignCenter)

    def addButton1(self):
        line_edit = QLineEdit("", self)
        line_edit.setGeometry(500, 300, 500, 30)
        line_edit.returnPressed.connect(self.do_action)
        self.mainLayout.addWidget(line_edit)

    def do_action(self):
        value = self.sender().text()
        self.Button2.clicked.connect(self.addButton2)

    def addButton2(self):
        self.Button2 = QPushButton("OK")
        self.Button2.setGeometry(500, 300, 500, 30)
        my_name = QAction("Ok", self)
        my_name.triggered.connect(self.click_func)
        self.Button2.addAction(my_name)
        self.mainLayout.addWidget(self.Button2, alignment=Qt.AlignmentFlag.AlignTop)

    def click_func(self):
        textboxValue = self.sender().text()
        QMessageBox.question(self, 'My Name', 'Hello!' + textboxValue, QMessageBox.Ok, QMessageBox.Ok)

    def init_ui(self):
        color_combo = QComboBox(self)
        colors = ['Red', 'Green', 'Blue', 'Yellow', 'Cyan', 'Magenta']
        color_combo.addItems(colors)
        color_combo.currentIndexChanged.connect(self.change_color)
        self.mainLayout.addWidget(color_combo)
        color_combo.setFixedSize(1500, 30)
        self.change_color(0)

    def change_color(self, index):
        color_name = self.sender().currentText() if self.sender() else "Cyan"
        color = QColor(color_name)
        self.setStyleSheet(f"background-color:{color.name()};")

    def radioUI(self):
        self.option1_radio = QRadioButton("Python", self)
        self.option2_radio = QRadioButton("Java", self)
        self.option3_radio = QRadioButton("C++", self)
        self.mainLayout.addWidget(self.option1_radio)
        self.mainLayout.addWidget(self.option2_radio)
        self.mainLayout.addWidget(self.option3_radio)

        self.selected_option_label = QLabel("Selected Option : None", self)
        self.mainLayout.addWidget(self.selected_option_label)

        self.option1_radio.toggled.connect(lambda: self.update_selected_option("Python"))
        self.option2_radio.toggled.connect(lambda: self.update_selected_option("Java"))
        self.option3_radio.toggled.connect(lambda: self.update_selected_option("C++"))

    def update_selected_option(self, option):
        if option:
            self.selected_option_label.setText(f"Selected Option: {option}")

    def slider(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.mainLayout.addWidget(self.slider)

        self.label = QLabel("Slider Value: 0", self)
        self.mainLayout.addWidget(self.label)

        self.slider.valueChanged.connect(self.update_label)

    def update_label(self):
        value = self.sender().value()
        self.label.setText(f"Slider Value: {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())