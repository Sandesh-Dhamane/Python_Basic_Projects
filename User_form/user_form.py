import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QRadioButton, QFileDialog, QMessageBox,QStyle
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class UserProfileForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('User Profile Form')

        # Header
        header_label = QLabel('User Profile Form')
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet('font-size: 20px; font-weight: bold; margin-bottom: 10px; align: center;')

        # Form Elements
        self.first_name_edit = QLineEdit()
        self.last_name_edit = QLineEdit()
        self.mobile_number_edit = QLineEdit()
        self.profile_photo_label = QLabel('No photo selected') 
        self.gender_male_radio = QRadioButton('Male')
        self.gender_female_radio = QRadioButton('Female')
        self.height_edit = QLineEdit()

        # Buttons
        select_photo_button = QPushButton('Select Photo')
        submit_button = QPushButton("Submit")
        submit_button.setFixedSize(100,50)

        # Form Layout
        form_layout = QFormLayout()
        form_layout.addRow('Enter First Name :', self.first_name_edit)
        form_layout.addRow('Enter Last Name :', self.last_name_edit)
        form_layout.addRow('Enter Mobile Number :', self.mobile_number_edit)
        form_layout.addRow('Select Profile Photo :', select_photo_button)
        form_layout.addRow(self.profile_photo_label)
        form_layout.addRow('Gender :', self.gender_male_radio)
        form_layout.addRow('', self.gender_female_radio)
        form_layout.addRow('Height(cm) :', self.height_edit)

        # Button Layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(submit_button)

        # Information Display
        self.info_display_label = QLabel()

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(header_label)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.info_display_label)  # Display entered information here

        self.setLayout(main_layout)

        # Connect Signals
        select_photo_button.clicked.connect(self.select_photo)
        submit_button.clicked.connect(self.submit_form)

        self.show()

    def select_photo(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter('Image files (*.png *.jpg *.bmp)')
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.profile_photo_label.setText(f'Selected Photo: {selected_file}')

    def submit_form(self):
        # Validation Checks
        if not self.first_name_edit.text() or not self.last_name_edit.text() or not self.mobile_number_edit.text():
            self.show_error_message('Please fill in all required fields')
            return

        if not self.mobile_number_edit.text().isdigit() or len(self.mobile_number_edit.text()) != 10:
            self.show_error_message('Invalid mobile number format. Please enter a 10-digit number')
            return

        # Successful Submission
        success_message = f' Form submitted Successfully.\n\nFirst Name: {self.first_name_edit.text()}\nLast Name: {self.last_name_edit.text()}\nMobile Number: {self.mobile_number_edit.text()}\nGender: {"Male" if self.gender_male_radio.isChecked() else "Female"}\nHeight: {self.height_edit.text()}'
        self.show_success_message(success_message)

    def show_error_message(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setWindowTitle('Error')
        error_dialog.setText(message)
        error_dialog.exec_()

    def show_success_message(self, message):
        self.info_display_label.setText(message)


if __name__== '__main__':
    app = QApplication(sys.argv)
    form = UserProfileForm()
    sys.exit(app.exec_())
