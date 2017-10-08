from PyQt5 import QtWidgets


class fristwindows(QtWidgets.QWidget):


    def __init__(self):
        super(fristwindows, self).__init__()


def mainwindows():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new = fristwindows()
    new.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    mainwindows()
