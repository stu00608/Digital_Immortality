# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_interface_start.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Digital_Immortality(object):
    def setupUi(self, Digital_Immortality):
        Digital_Immortality.setObjectName("Digital_Immortality")
        Digital_Immortality.resize(576, 444)
        self.centralwidget = QtWidgets.QWidget(Digital_Immortality)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ICON = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ICON.sizePolicy().hasHeightForWidth())
        self.ICON.setSizePolicy(sizePolicy)
        self.ICON.setMaximumSize(QtCore.QSize(16777215, 200))
        self.ICON.setText("")
        self.ICON.setPixmap(QtGui.QPixmap("bot_icon.png"))
        self.ICON.setAlignment(QtCore.Qt.AlignCenter)
        self.ICON.setObjectName("ICON")
        self.verticalLayout.addWidget(self.ICON)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.chooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.chooseButton.setObjectName("chooseButton")
        self.verticalLayout.addWidget(self.chooseButton)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setEnabled(False)
        self.startButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.startButton.setCheckable(False)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.settingButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.settingButton.setObjectName("settingButton")
        self.verticalLayout.addWidget(self.settingButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Digital_Immortality.setCentralWidget(self.centralwidget)

        self.retranslateUi(Digital_Immortality)
        QtCore.QMetaObject.connectSlotsByName(Digital_Immortality)

    def retranslateUi(self, Digital_Immortality):
        _translate = QtCore.QCoreApplication.translate
        Digital_Immortality.setWindowTitle(_translate("Digital_Immortality", "Digital Immortality"))
        self.label.setText(_translate("Digital_Immortality", "Digital Immortality"))
        self.chooseButton.setText(_translate("Digital_Immortality", "????????????"))
        self.startButton.setText(_translate("Digital_Immortality", "??????"))
        self.settingButton.setText(_translate("Digital_Immortality", "??????"))
