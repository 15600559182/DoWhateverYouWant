#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a tooltip on a window and a button.

author:Jan Bodnar
webstie: zetcode.com
lash edited: January 2015

"""

import sys  # 导入系统包
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont  # 导入pyqt5字体


class Example(QWidget):  # 创建类
    def __init__(self):  # 创建构造方法
        super().__init__()  # 继承默认的构造方法

        self.initUI()  # 使用自己写的初始化图形界面方法

    def initUI(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))  # 这个静态方法设置了用于提示框的字体。我们使用10px大小的SansSerif字体。

        self.setToolTip('This is a <b>QWidget</b> widget')  # 提示框你标题

        btn = QPushButton('Button', self)  # 创建一个按钮
        btn.setToolTip('This is a <b>fQPushButton</b> widget')  # 按钮上创建提示框文本title
        btn.resize(btn.sizeHint())  # 调整按钮 设置推荐大小
        btn.move(50, 50)  # 按钮定位

        self.setGeometry(300, 300, 300, 200)  # 设置  窗口位置x,y 窗口大小
        self.setWindowTitle('Tooltips')  # 设置窗口提示
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用（Application）对象
    ex = Example()
    sys.exit(app.exec_())  # 一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。
