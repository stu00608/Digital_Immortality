# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resource/chat_interface_setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(500, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Setting.sizePolicy().hasHeightForWidth())
        Setting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        Setting.setFont(font)
        Setting.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Setting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(Setting)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botImage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botImage.sizePolicy().hasHeightForWidth())
        self.botImage.setSizePolicy(sizePolicy)
        self.botImage.setMaximumSize(QtCore.QSize(16777215, 30))
        self.botImage.setObjectName("botImage")
        self.horizontalLayout.addWidget(self.botImage)
        self.chooseButton1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseButton1.sizePolicy().hasHeightForWidth())
        self.chooseButton1.setSizePolicy(sizePolicy)
        self.chooseButton1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.chooseButton1.setObjectName("chooseButton1")
        self.horizontalLayout.addWidget(self.chooseButton1)
        self.botImagePath = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botImagePath.sizePolicy().hasHeightForWidth())
        self.botImagePath.setSizePolicy(sizePolicy)
        self.botImagePath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.botImagePath.setAlignment(QtCore.Qt.AlignCenter)
        self.botImagePath.setObjectName("botImagePath")
        self.horizontalLayout.addWidget(self.botImagePath)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.userImage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userImage.sizePolicy().hasHeightForWidth())
        self.userImage.setSizePolicy(sizePolicy)
        self.userImage.setMaximumSize(QtCore.QSize(16777215, 30))
        self.userImage.setObjectName("userImage")
        self.horizontalLayout_2.addWidget(self.userImage)
        self.chooseButton2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseButton2.sizePolicy().hasHeightForWidth())
        self.chooseButton2.setSizePolicy(sizePolicy)
        self.chooseButton2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.chooseButton2.setObjectName("chooseButton2")
        self.horizontalLayout_2.addWidget(self.chooseButton2)
        self.userImagePath = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userImagePath.sizePolicy().hasHeightForWidth())
        self.userImagePath.setSizePolicy(sizePolicy)
        self.userImagePath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.userImagePath.setAlignment(QtCore.Qt.AlignCenter)
        self.userImagePath.setObjectName("userImagePath")
        self.horizontalLayout_2.addWidget(self.userImagePath)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fontSize = QtWidgets.QLabel(self.centralwidget)
        self.fontSize.setObjectName("fontSize")
        self.horizontalLayout_4.addWidget(self.fontSize)
        self.label_2n = QtWidgets.QLabel(self.centralwidget)
        self.label_2n.setText("")
        self.label_2n.setObjectName("label_2n")
        self.horizontalLayout_4.addWidget(self.label_2n)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setMaximumSize(QtCore.QSize(100, 40))
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_3.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setMaximumSize(QtCore.QSize(100, 40))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Setting.setCentralWidget(self.centralwidget)

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "設定"))
        self.botImage.setText(_translate("Setting", "機器人照片："))
        self.chooseButton1.setText(_translate("Setting", "選擇檔案"))
        self.botImagePath.setText(_translate("Setting", "Path"))
        self.userImage.setText(_translate("Setting", "使用者照片："))
        self.chooseButton2.setText(_translate("Setting", "選擇檔案"))
        self.userImagePath.setText(_translate("Setting", "Path"))
        self.fontSize.setText(_translate("Setting", "    字體大小："))
        self.okButton.setText(_translate("Setting", "確認"))
        self.cancelButton.setText(_translate("Setting", "取消"))
