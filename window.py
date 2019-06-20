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
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_inPut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inPut.setGeometry(QtCore.QRect(550, 160, 101, 31))
        self.pushButton_inPut.setStyleSheet("background-image: url(:/png/import.png);")
        self.pushButton_inPut.setText("")
        self.pushButton_inPut.setObjectName("pushButton_inPut")
        self.pushButton_conversion = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_conversion.setGeometry(QtCore.QRect(550, 420, 101, 101))
        self.pushButton_conversion.setStyleSheet("background-image: url(:/png/conversion.png);")
        self.pushButton_conversion.setText("")
        self.pushButton_conversion.setObjectName("pushButton_conversion")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 350, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.iput_image = QtWidgets.QLabel(self.centralwidget)
        self.iput_image.setGeometry(QtCore.QRect(28, 85, 500, 500))
        self.iput_image.setScaledContents(True)
        self.iput_image.setObjectName("iput_image")
        self.output_image = QtWidgets.QLabel(self.centralwidget)
        self.output_image.setGeometry(QtCore.QRect(674, 85, 500, 500))
        self.output_image.setScaledContents(True)
        self.output_image.setObjectName("output_image")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(550, 220, 101, 94))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
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
        self.comboBox.setItemText(0, _translate("MainWindow", "清晰"))
        self.comboBox.setItemText(1, _translate("MainWindow", "一般"))
        self.comboBox.setItemText(2, _translate("MainWindow", "字符"))
        self.iput_image.setText(_translate("MainWindow", "图片1"))
        self.output_image.setText(_translate("MainWindow", "图片2"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

import img_qc_rc
