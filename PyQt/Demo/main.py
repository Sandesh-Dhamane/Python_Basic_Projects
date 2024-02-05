import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        self.setGeometry(500,300,500,300)

        self.mainLayout = QVBoxLayout(self)

        self.setLayout(self.mainLayout)

        self.LabelUI()

    def LabelUI(self):
        self.label = QLabel ("Core2web")

        self.mainLayout.addWidget(self.label,0,Qt.AlignmentFlag.AlignCenter)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    main_Window = Mainwindow()
    main_Window.show()
    sys.exit(app.exec_()) 