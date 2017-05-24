from PySide.QtCore import *
from PySide.QtGui import *


class CalendarDoctor(QWidget):
    def __init__(self):
        super(CalendarDoctor, self).__init__()
        self.setWindowTitle("Calendar Widget")
        self.createCalendar()
        self.setCalendar()
        layoutGroupBox = QGridLayout()
        layoutGroupBox.addWidget(self.calendarGroupBox, 0, 0)
        layoutGroupBox.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(layoutGroupBox)

        self.layout = QGridLayout()
        self.layout.addWidget(self.calendar, 0, 0, Qt.AlignCenter)
        self.layout.setRowMinimumHeight(0, self.calendar.sizeHint().height())
        self.layout.setColumnMinimumWidth(0, self.calendar.sizeHint().width())
        self.calendarGroupBox.setLayout(self.layout)

        self.calendar.selectionChanged.connect(self.selectedDateChanged)

    def setCalendar(self):
        #set select mode
        self.calendar.setSelectionMode(
            QCalendarWidget.SelectionMode(QCalendarWidget.SingleSelection))
        #set horizontal
        self.calendar.setHorizontalHeaderFormat(
            QCalendarWidget.HorizontalHeaderFormat(
                QCalendarWidget.LongDayNames))
        #set vertical
        self.calendar.setVerticalHeaderFormat(
            QCalendarWidget.VerticalHeaderFormat(
                QCalendarWidget.NoVerticalHeader))

    def selectedDateChanged(self):
        print(self.calendar.selectedDate())

    def weekdayFormatChanged(self):
        format = QTextCharFormat()
        format.setForeground(Qt.black)
        self.calendar.setWeekdayTextFormat(Qt.Monday, format)
        self.calendar.setWeekdayTextFormat(Qt.Tuesday, format)
        self.calendar.setWeekdayTextFormat(Qt.Wednesday, format)
        self.calendar.setWeekdayTextFormat(Qt.Thursday, format)
        self.calendar.setWeekdayTextFormat(Qt.Friday, format)

    def weekendFormatChanged(self):
        format = QTextCharFormat()
        format.setForeground(Qt.red)
        self.calendar.setWeekdayTextFormat(Qt.Saturday, format)
        self.calendar.setWeekdayTextFormat(Qt.Sunday, format)

    def reformatHeaders(self):
        format = QTextCharFormat()
        format.setForeground(Qt.black)
        self.calendar.setHeaderTextFormat(format)

    def createCalendar(self):
        self.calendarGroupBox = QGroupBox("Calendar Doctor")
        self.calendar = QCalendarWidget()
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QDate(3000, 1, 1))
        self.calendar.setGridVisible(False)
        self.reformatHeaders()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = CalendarDoctor()
    window.show()

    sys.exit(app.exec_())