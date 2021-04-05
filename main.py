import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import chat_interface_start as chat


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = chat.Ui_Digital_Immortality()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())