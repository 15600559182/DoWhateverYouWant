#!/usr/bin/pthon3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 totorial

This propgram creates a quit
button. When we press the button,
the application termaintes.

author:Jan Bodnar
website: zetcode.com
last edited:January 2015

"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)#创建一个按钮
        qbtn.clicked.connect(QCoreApplication.instance().quit)#为此按钮绑定鼠标点击事件
        qbtn.resize(qbtn.sizeHint())#设置按钮大小为 合适大小
        qbtn.move(50, 50)#窗口

        self.setGeometry(300, 300, 250, 150)#设置画布
        self.setWindowTitle('Quit button')#设置标题
        self.show()#内存中实例化一个


if __name__ == '__main__':
    app = QApplication(sys.argv)#声明一个applicaiton
    ex = Example()#创建一个空参数
    sys.exit(app.exec_())#干净的退出
