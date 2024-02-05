import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QTabWidget, QVBoxLayout,QWidget, QApplication, QDesktopWidget
from PyQt5.QtGui import QColor, QIcon
from nbconvert import QtPDFExporter
from PythonInfo import C2W_PythonInfo

# from pyi import C2W_PythonInfo
class C2W_Home(object):
    layout1 = None
    count = 0
    WidgetTemp=0
    def c2w_openLink(self,event):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://www.core2web.in/"))

    def setupUi(self,widget):
        self.c2w_WidgetTemp=widget
        desktop=QDesktopWidget()

        #Get the primary screen (monitor)
        primary_screen = desktop.screenGeometry(desktop.primaryScreen())

        #Retrive the width of the monitor
        monitor_width = primary_screen.width()
        monitor_height = primary_screen.width()
        widget.setObjectName("widget")
        widget.resize(monitor_width,monitor_height)
        self.c2w_Widget = QtWidgets.QWidget(widget)
        self.c2w_Widget.setGeometry(QtCore.QRect(0,0,monitor_width,50))
        self.c2w_Widget.setStyleSheet("background:0E1D35;")
        self.c2w_Widget.setObjectName("Widget")

        #Create a QLAbel for the image
        self.c2w_imageLabel1 = QtWidgets.QLabel(self.c2w_Widget)
        self.c2w_imageLabel1.setGeometry(QtCore.QRect(15,0,200,50))
        self.c2w_imageLabel1.setObjectName("imageLabel")

        #Load an image using Qpixmap
        pixmap1 = QtGui.QPixmap('./assets/images/Group 943logo.png')

        #set style on image
        #set the pixmap to the QLabel
        self.c2w_imageLabel1.setPixmap(pixmap1)
        self.c2w_imageLabel1.mouseDoubleClickEvent=self.c2w_openLink
        self.c2w_aboutbtn=QtWidgets.QPushButton(self.c2w_Widget)
        self.c2w_aboutbtn.setGeometry(QtCore.QRect(int(monitor_width/1.13),5,140,40))
        self.c2w_aboutbtn.setStyleSheet("background:red;font-size:20px;border-radius:15px;color:white;")
        self.c2w_aboutbtn.setObjectName("aboutbtn")
        self.c2w_aboutbtn.clicked.connect(self.c2w_aboutCall)

        self.c2w_frame = QtWidgets.QFrame(widget)
        self.c2w_frame.setGeometry(QtCore.QRect(0,50,monitor_width,monitor_height))
        self.c2w_frame.setStyleSheet("background:#2B3D5B;\n""font-style:poppins")
        self.c2w_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.c2w_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c2w_frame.setObjectName("Frame")
        self.c2w_Widget_2 = QtWidgets.QWidget(self.c2w_frame)
        self.c2w_Widget_2.setGeometry(QtCore.QRect(int(monitor_width/2.55),int(monitor_height/6),321,370))
        #self.c2w_Widget_2.setStyleSheet("background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0 rgba(255,235,235,206),stop:0.35 rgba(255,188,188,80),stop:0.4 rgba(255,162,162,80),stop:0.425 rgba(255,132,132,156),stop:0.44 rgba(252,128,128,80),stop:1 rgba(255,255,255,0))")
        self.c2w_Widget_2.setObjectName("widget_2")

        # Create a QLabel for the image
        self.c2w_imageLabel = QtWidgets.QLabel(self.c2w_Widget_2)
        self.c2w_imageLabel.setGeometry(QtCore.QRect(-80, -10, 400, 400))
        self.c2w_imageLabel.setObjectName("imageLabel")

        # Load an image of python logo using QPixmap
        pixmap = QtGui.QPixmap('./assets/images/copy.png')
        # Set Style on image
        # Set the pixmap to the QLabel
        self.c2w_imageLabel.setPixmap(pixmap)

        # Shadow for button
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setBlurRadius(10)
        self.c2w_pushButton = QtWidgets.QPushButton(self.c2w_Widget_2)
        self.c2w_pushButton.setGeometry(QtCore.QRect(85, 300, 140, 45))
        self.c2w_pushButton.setStyleSheet("background:#0E1D35; font-size:20px;border-radius:15px; color:white;")
        self.c2w_pushButton.setGraphicsEffect(shadow)
        self.c2w_pushButton.setObjectName("pushButton")

        # Calling another by Click button
        self.c2w_ui = C2W_PythonInfo()
        self.c2w_pushButton.clicked.connect(self.c2w_open_python_info)
        self.retranslateUi(widget)
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','assets', 'images', 'core2web Logo.png'))
        widget.setWindowIcon(QIcon(icon_path))
    def c2w_open_python_info(self):
        self.c2w_ui.infoPage(self.c2w_Widget.parent())
    def c2w_aboutCall(self):
        pass
    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Python Library by C2W"))
        self.c2w_pushButton.setText(_translate("Widget", "Click Here"))
        self.c2w_aboutbtn.setText(_translate("Widget", "Enquire us"))