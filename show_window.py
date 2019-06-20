from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog
from PyQt5 import QtGui
import sys
import  _thread
import time
import  conversion


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
    #打开图片文件
    def openFile(self):
        openfile_name = QFileDialog.getOpenFileName()
        if openfile_name[0] !="":
            self.input_path = openfile_name[0]
            self.show_input_img(self.input_path)
    #显示输入的图片
    def show_input_img(self,file_path):
        input_img = QtGui.QPixmap(file_path)
        self.iput_image.setPixmap(input_img)#设置图片

    #启动图片转换
    def start_conversion(self):
        if hasattr(main,"input_path"):
            #self.gif = QtGui.Qmovie("loding.gif")
            #self.gif = QtGui.QMovie('loding.gif')
            #self.loading.setMovie(self.gif)
            #self.gif.start()
            #_thread.start_new_thread(ambda: self.is_conversion(main.input_path),())
            _thread.start_new_thread(lambda: self.is_conversion(main.input_path), ())
        else:
            print("没有图片")

    def is_conversion(self,file_path):
        t = str(int(time.time()))
        #转换后的字符画图路径
        export_path = "export_img"+t+".png"
        input_char = main.textEdit.toPlainText()
        definition = main.comboBox.currentText()

        is_over = conversion.picture_conversion(file_path,export_path,input_char,definition)
        if is_over == False:
            #self.loding.clear()
            #self.loding.clear()  # 转换完毕就将等待gif图片清理掉
            main.show_export_img(export_path)


    def show_export_img(self,file_path):
        export_img = QtGui.QPixmap(file_path)
        self.output_image.setPixmap(export_img)




if __name__ == "__main__":
    #入口函数
    app = QApplication(sys.argv)
    main = Main()
    main.pushButton_inPut.clicked.connect(main.openFile)
    main.pushButton_conversion.clicked.connect(main.start_conversion)
    main.show()
    sys.exit(app.exec())