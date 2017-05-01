from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class Tab1Calendar(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setUI()
        self.setConnect()

    def setUI(self):
        loader = QUiLoader()
        form = loader.load('./view/Tab1_CalendarUI.ui', self)
        self.calendar = form.findChild(QCalendarWidget, 'calendarWidget')
        self.labelDate = form.findChild(QLabel, 'label_date')

    def setConnect(self):
        c = QCalendarWidget()

        #self.calendar.


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    tab1_widget = Tab1Calendar()
    tab1_widget.show()
    sys.exit(app.exec_())
