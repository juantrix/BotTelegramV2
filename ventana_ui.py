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
        MainWindow.resize(816, 222)
        MainWindow.setMinimumSize(QtCore.QSize(816, 222))
        MainWindow.setMaximumSize(QtCore.QSize(816, 222))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
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
        self.CheckBorrar.setGeometry(QtCore.QRect(670, 30, 91, 31))
        self.CheckBorrar.setObjectName("CheckBorrar")
        self.ApiKeyText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ApiKeyText.setGeometry(QtCore.QRect(10, 150, 261, 31))
        self.ApiKeyText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ApiKeyText.setObjectName("ApiKeyText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 130, 47, 13))
        self.label.setObjectName("label")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(420, 150, 181, 31))
        self.StartButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(17, 255, 0);")
        self.StartButton.setObjectName("StartButton")
        self.ChatID = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ChatID.setGeometry(QtCore.QRect(300, 150, 101, 31))
        self.ChatID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ChatID.setObjectName("ChatID")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 130, 47, 13))
        self.label_2.setObjectName("label_2")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(620, 150, 181, 31))
        self.stopButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 55, 55);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.stopButton.setObjectName("stopButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
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
        self.label_2.setText(_translate("MainWindow", "Chat-ID"))
        self.stopButton.setText(_translate("MainWindow", "stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

