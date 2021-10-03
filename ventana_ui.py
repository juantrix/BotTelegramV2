# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CheckFotos = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckFotos.setGeometry(QtCore.QRect(30, 30, 70, 17))
        self.CheckFotos.setObjectName("CheckFotos")
        self.CheckVideos_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckVideos_2.setGeometry(QtCore.QRect(30, 60, 70, 17))
        self.CheckVideos_2.setObjectName("CheckVideos_2")
        self.CheckAudios = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckAudios.setGeometry(QtCore.QRect(30, 90, 70, 17))
        self.CheckAudios.setObjectName("CheckAudios")
        self.CheckBorrar = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckBorrar.setGeometry(QtCore.QRect(640, 20, 141, 17))
        self.CheckBorrar.setObjectName("CheckBorrar")
        self.ApiKeyText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ApiKeyText.setGeometry(QtCore.QRect(10, 180, 371, 31))
        self.ApiKeyText.setObjectName("ApiKeyText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 160, 47, 13))
        self.label.setObjectName("label")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(460, 180, 321, 31))
        self.StartButton.setObjectName("StartButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CheckFotos.setText(_translate("MainWindow", "Fotos"))
        self.CheckVideos_2.setText(_translate("MainWindow", "Videos"))
        self.CheckAudios.setText(_translate("MainWindow", "Audios"))
        self.CheckBorrar.setText(_translate("MainWindow", "Borrar Media"))
        self.label.setText(_translate("MainWindow", "API-KEY"))
        self.StartButton.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

