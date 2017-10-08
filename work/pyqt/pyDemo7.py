from PyQt5 import QtWidgets


# 从PyQt库导入QtWidget通用窗口类
class mywindow(QtWidgets.QWidget):


    # 自己建一个mywindows类，以class开头，mywindows是自己的类名，
    # （QtWidgets.QWidget）是继承QtWidgets.QWidget类方法，
    # 定义类或函数不要忘记':'符号，判断语句也必须以':'结尾！
    def __init__(self):
        # def是定义函数（类方法）了，同样第二个__init__是函数名
        # (self)是pyqt类方法必须要有的，代表自己，相当于java，c++中的this
        # 其实__init__是析构函数，也就是类被创建后就会预先加载的项目
        super(mywindow, self).__init__()


# 这里我们要重载一下mywindows同时也包含了QtWidgets.QWidget的预加载项

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # pyqt窗口必须在QApplication方法中使用，
    # 要不然会报错 QWidget: Must construct a QApplication before a QWidget
    windows = mywindow()
    # 生成过一个实例（对象）, windows是实例（对象）的名字，可以随便起！
    # mywindows（）是我们上面自定义的类
    windows.show()
    # 有了实例，就得让他显示这里的show()是QWidget的方法，用来显示窗口的！
    sys.exit(app.exec_())
    # 启动事件循环 
