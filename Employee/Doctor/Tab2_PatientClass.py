from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class Tab2Patient(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setUI()
        self.setConnect()

    def setUI(self):
        loader = QUiLoader()
        form = loader.load('./view/Tab2_Patient.ui', self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    tab1_widget = Tab2Patient()
    tab1_widget.show()
    sys.exit(app.exec_())
