import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
class NameInputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle("Input Output")
        self.setGeometry(500, 100, 500, 300)
        #self.create_menus()

    def init_ui(self):
        # Create a QVBoxLayout
        layout = QVBoxLayout()
        #self.mainLayout = QVBoxLayout(self)


        # Create a QLabel to instruct the user
        label = QLabel('Enter your name', self)
        layout.addWidget(label,0,Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Create a QLineEdit for the user to enter their name
        self.name_line_edit = QLineEdit(self)
        layout.addWidget(self.name_line_edit)

        # Create an "OK" button to submit the name
        ok_button = QPushButton('OK', self)
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        # Set the layout for the dialog
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Create the NameInputDialog instance
    name_input_dialog = NameInputDialog()
    
    # Show the NameInputDialog
    name_input_dialog.exec_()
    result = name_input_dialog.exec_()
    sys.exit(app.exec_())