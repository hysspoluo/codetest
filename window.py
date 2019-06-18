# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_inPut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inPut.setGeometry(QtCore.QRect(450, 170, 101, 28))
        self.pushButton_inPut.setStyleSheet("background-image: url(:/png/C:/Users/lenovo/Desktop/第6章DIY字符画——源码/06/可执行程序/img/import.png);")
        self.pushButton_inPut.setText("")
        self.pushButton_inPut.setObjectName("pushButton_inPut")
        self.pushButton_conversion = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_conversion.setGeometry(QtCore.QRect(450, 390, 101, 101))
        self.pushButton_conversion.setStyleSheet("background-image: url(:/png/C:/Users/lenovo/Desktop/第6章DIY字符画——源码/06/可执行程序/img/conversion.png);")
        self.pushButton_conversion.setText("")
        self.pushButton_conversion.setObjectName("pushButton_conversion")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(440, 220, 121, 87))
        self.textEdit.setStyleSheet("color:rgb(255,0,0);\n"
"placeholderText:请输入字符")
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(440, 340, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.iput_image = QtWidgets.QLabel(self.centralwidget)
        self.iput_image.setGeometry(QtCore.QRect(70, 180, 261, 311))
        self.iput_image.setScaledContents(True)
        self.iput_image.setObjectName("iput_image")
        self.output_image = QtWidgets.QLabel(self.centralwidget)
        self.output_image.setGeometry(QtCore.QRect(640, 160, 261, 311))
        self.output_image.setScaledContents(True)
        self.output_image.setObjectName("output_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 26))
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
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请输入字符</p></body></html>"))
        self.iput_image.setText(_translate("MainWindow", "TextLabel"))
        self.output_image.setText(_translate("MainWindow", "TextLabel"))

import img_qc_rc
