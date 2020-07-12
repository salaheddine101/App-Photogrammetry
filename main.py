# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import background_rc

from affine import Ui_Affine
from helmert import Ui_Helmert
from projective import Ui_Projective

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 540)
        MainWindow.setMinimumSize(QtCore.QSize(100, 100))
        MainWindow.setMaximumSize(QtCore.QSize(850, 540))
        MainWindow.setStyleSheet("background-image: url(:/.png/main-v5.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(440, 230, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(91, 53, 71);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 230, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 89, 73);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda: self.choix_transformation(self.comboBox.currentText()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orientation Intérieure"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Transformation Helmert"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Transformation Affine"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Transformation Projective"))
        self.pushButton.setText(_translate("MainWindow", "VALIDER"))


    def choix_transformation(self, choix):
        if choix == "Transformation Helmert":
            self.Helmert = QtWidgets.QMainWindow()
            self.ui = Ui_Helmert()
            self.ui.setupUi(self.Helmert)
            self.Helmert.show()

        if choix == "Transformation Affine":
            self.Affine = QtWidgets.QMainWindow()
            self.ui = Ui_Affine()
            self.ui.setupUi(self.Affine)
            self.Affine.show()

        if choix == "Transformation Projective":
            self.Projective = QtWidgets.QMainWindow()
            self.ui = Ui_Projective()
            self.ui.setupUi(self.Projective)
            self.Projective.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
