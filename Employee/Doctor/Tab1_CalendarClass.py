from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader

class Tab1Calendar(QWidget):
    def __init__(self, user, parent=None):
        QWidget.__init__(self, None)
        self.user = user
        self.parent = parent
        self.initUI()
        self.initLayout()
        self.initButton()
        self.initConnect()

    def initUI(self):
        self.tab1 = QUiLoader().load('./Employee/Doctor/View/Tab1_CalendarUI.ui', self)
        self.calendar = self.tab1.findChild(QCalendarWidget, 'calendarWidget')
        self.labelDate = self.tab1.findChild(QLabel, 'label_date')
        self.taskView = self.tab1.findChild(QListView, 'listView')


    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tab1)
        self.setLayout(layout)

    def initButton(self):
        pass

    def initConnect(self):
        self.calendar.selectionChanged.connect(self.selectedDate)

    def selectedDate(self):
        date = self.calendar.selectedDate().toString()
        self.labelDate.setText(date)
        date = date.split()
        self.taskView.setModel(self.createdModel(date[1], date[2]))

    def createdModel(self, month, day):
        model = QStringListModel()
        print(month + day)
        text = ["Atichat", "Fern"]
        model.setStringList(text)
        return model


if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    tab1_widget = Tab1Calendar()
    tab1_widget.show()
    sys.exit(app.exec_())
