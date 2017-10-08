from PyQt5 import QtWidgets
from pyDemo9 import fristwindows

if __name__ == '__main__':
    import sys

    print(10)
    app = QtWidgets.QApplication(sys.argv)
    new = fristwindows()
    new.show()
    sys.exit(app.exec())

