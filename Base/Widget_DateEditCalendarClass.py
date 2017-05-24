from PySide.QtCore import QEvent, Qt
from PySide.QtGui import QWidget, QGridLayout, QDateEdit, QSpacerItem, QSizePolicy, QApplication


class DateEditCalendar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setDateEdit()
        self.show()

    def initUI(self):
        self.dateEdit = QDateEdit()
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.dateEdit, 0, 0)
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(layout)

    def setDateEdit(self):
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(self)
        self.dateEdit.calendarWidget().setFirstDayOfWeek(Qt.Monday)

    def eventFilter(self, obj, event):
        if obj == self.dateEdit.calendarWidget() and event.type() == QEvent.Show:
            pos = self.dateEdit.mapToGlobal(self.dateEdit.geometry().bottomRight())
            width = self.dateEdit.calendarWidget().window().width()
            self.dateEdit.calendarWidget().window().move(pos.x() - width, pos.y())
        return False


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = DateEditCalendar()
    exit(app.exec_())