from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog
from PyQt5 import QtGui
import sys
import  _thread
import time

#主窗体初始化类

class Main(QMainWindow,Ui_MainWindow):#两个窗口类
    def __init__(self):
        super(Main,self).__init__()#初始化类对象,调用父类的构造函数
        self.setupUi(self)
        #开启自动填充背景
        #新增一些手动添加背景的操作
        self.centralwidget.setAutoFillBackground(True)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap('bg.png'))) #设置背景
        #加载背景
        self.centralwidget.setPalette(palette)
        input_image = QtGui.QPixmap('input_test.png')
        self.iput_image.setPixmap(input_image)#设置初始化图片
        output_image = QtGui.QPixmap('output_test.png')
        self.output_image.setPixmap(output_image)


if __name__ == "__main__":
    #入口函数
    app = QApplication(sys.argv)
    main1 = Main()
    main1.show()
    sys.exit(app.exec())