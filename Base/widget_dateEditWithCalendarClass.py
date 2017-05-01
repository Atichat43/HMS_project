import sys
from PySide.QtCore import QEvent
from PySide.QtGui import QWidget, QGridLayout, QDateEdit, QSpacerItem, QSizePolicy, QApplication


class DateEditCalendar(QWidget):
    def __init__(self):
        super().__init__()
        self.setUi()
        self.show()

    def setUi(self):
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(self)
        layout.addWidget(self.dateEdit, 0, 0)
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(layout)

    def eventFilter(self, obj, event):
        if obj == self.dateEdit.calendarWidget() and event.type() == QEvent.Show:
            pos = self.dateEdit.mapToGlobal(self.dateEdit.geometry().bottomRight())
            width = self.dateEdit.calendarWidget().window().width()
            self.dateEdit.calendarWidget().window().move(pos.x() - width, pos.y())
        return False

def main():
    app = QApplication(sys.argv)
    win = DateEditCalendar()
    exit(app.exec_())

if __name__ == "__main__":
    main()