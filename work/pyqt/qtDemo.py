#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5创建了一个简单的窗口。

作者: Jan Bodnar
网站: zetcode.com
最后一次编辑: January 2015
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1600, 800)#画布大小
    w.move(200, 100)#画布位置
    w.setWindowTitle('Simple')#窗口标题
    w.show()#显示一个widget，此对象在内存创建

    sys.exit(app.exec_())#进入主循环，sys.exit区别不留垃圾的退出
