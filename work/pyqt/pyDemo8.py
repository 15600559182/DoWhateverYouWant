from PyQt5 import QtWidgets


class fristWindows(QtWidgets.QWidget):
    def __init__(self):
        super(fristWindows, self).__init__()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    new = fristWindows()
    new.show()
    sys.exit(app.exec_())
