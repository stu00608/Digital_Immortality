# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

msg_count = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(110, 10, 671, 441))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 470, 551, 71))
        self.textEdit.setObjectName("textEdit")

        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(670, 470, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sendButton.setFont(font)
        self.sendButton.setCheckable(False)
        self.sendButton.setObjectName("sendButton")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 89, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #---self-config---#

        self.msg_count = 0

        # self.formLayout = QtWidgets.QFormLayout()
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setHorizontalSpacing(3)
        self.gridlayout.setVerticalSpacing(5)

        

        self.groupBox = QtWidgets.QGroupBox()

        self.sendButton.clicked.connect(self.on_send)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))

    def on_send(self):
        msg = self.textEdit.toPlainText()
        if(msg==''):
            return
        # if(len(msg)>=10):
        #     msg = list(msg)
        #     i=n=10
        #     while i < len(msg):
        #         msg.insert(i, 'x')
        #         i += (n+1)
        #     msg=''.join(msg)

        self.send_message(0,msg)
        self.send_message(1,"yes")
        

    

    def send_message(self,who,msg):
        # who==0 -> usr
        if(who):
            photo_path = 'bot.png'
        else:
            photo_path = 'user.jpg'

        photo = QLabel()
        pixmap = QPixmap(photo_path)
        smaller_pixmap = pixmap.scaled(80, 80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        photo.setPixmap(smaller_pixmap)
        
        text = QLabel()
        font = QtGui.QFont()
        font.setPointSize(20)
        text.setFont(font)
        text.setText(msg)
        text.setWordWrap(True)

        pos = QLabel()

        if(who):
            self.gridlayout.addWidget(photo,self.msg_count,0,alignment=QtCore.Qt.AlignLeft)
            self.gridlayout.addWidget(text,self.msg_count,1,alignment=QtCore.Qt.AlignLeft)
            self.gridlayout.addWidget(pos,self.msg_count,2,alignment=QtCore.Qt.AlignCenter)
        else:
            self.gridlayout.addWidget(pos,self.msg_count,0,alignment=QtCore.Qt.AlignCenter)
            self.gridlayout.addWidget(text,self.msg_count,1,alignment=QtCore.Qt.AlignRight)
            self.gridlayout.addWidget(photo,self.msg_count,2,alignment=QtCore.Qt.AlignRight)
        
        self.groupBox.setLayout(self.gridlayout)
        self.scrollArea.setWidget(self.groupBox)
        
        self.msg_count += 1


