from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
from collections import defaultdict
import Setting as s


class Tab1Calendar(QWidget):
    def __init__(self, user, parent=None):
        QWidget.__init__(self, None)
        self.user = user
        self.parent = parent
        self.initUI()
        self.initLayout()
        self.initConnect()
        self.createdModelForCalendar()
        #self.fordevCheckAppointment()

    def initUI(self):
        self.tab1 = QUiLoader().load('./Employee/Doctor/View/Tab1_CalendarUI.ui', self)
        self.calendar = self.tab1.findChild(QCalendarWidget, 'calendarWidget')
        self.labelDate = self.tab1.findChild(QLabel, 'label_date')
        self.taskView = self.tab1.findChild(QListView, 'listView')

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tab1)
        self.setLayout(layout)

    def initConnect(self):
        self.calendar.selectionChanged.connect(self.selectedDate)

    def selectedDate(self):
        date = self.calendar.selectedDate().toString()
        self.labelDate.setText(date)
        date = date.split()
        model = self.createdModel(s.Month[date[1]].value, date[2])
        self.taskView.setModel(model)

    def createdModel(self, month, day):
        #list HEAD []
        model = QStringListModel()
        lst_task = []
        for appointment in self.appointment[month]:
            if appointment.date.day == day:
                text = appointment.getDataForCalendarDcotor()
                lst_task.append('\n'.join(text))
        model.setStringList(lst_task)
        return model

    def createdModelForCalendar(self):
        all_appointment = self.parent.getAppointment()
        self.appointment = defaultdict(list)
        for appointment in all_appointment:
            self.appointment[int(appointment.date.month)].append(appointment)

if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    tab1_widget = Tab1Calendar()
    tab1_widget.show()
    sys.exit(app.exec_())
