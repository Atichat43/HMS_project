import sys

from PySide.QtCore import QRegExp, QPoint, QEvent
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader

from Base.Dialog_MsgBox import ConfirmMsgClass
from Base import widget_dateEditWithCalendarClass
from Patient import PatientClass
import AppointmentClass


class newPatientDialog(QDialog):
    def __init__(self, parent=None):
        super(newPatientDialog, self).__init__(parent)
        self.setGeometry(300, 200, 400, 400)
        self.loader = QUiLoader()
        self.ui = self.loader.load('./view/Widget_AppointmentUI.ui', self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.ui)
        self.initUI()

    def initUI(self):
        self.comboBoxType = self.ui.findChild(QComboBox, "comboBox_type")
        self.dateEdit = self.ui.findChild(QDateEdit, "dateEdit")
        self.setDateEdit()
        self.comboBoxTime = self.ui.findChild(QComboBox, "comboBox_time")
        self.b_save = self.ui.findChild(QPushButton, "b_save")
        # self.b_cancel = self.ui.findChild(QPushButton, "b_cancel")
        self.b_save.clicked.connect(self.save)
        # self.b_cancel.clicked.connect(self.cancel)

    def setDateEdit(self):
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.dateEdit.calendarWidget() and event.type() == QEvent.Show:
            pos = self.dateEdit.mapToGlobal(self.dateEdit.geometry().bottomRight())
            width = self.dateEdit.calendarWidget().window().width()
            self.dateEdit.calendarWidget().window().move(pos.x() - width, pos.y())
        return False

    def setLineEdit(self):
        pass

    def save(self):
        # text = []
        # for lineEdit in self.setInput:
        #     text.append(lineEdit.text())
        # save to database
        d = QDateEdit()
        # d.dateTimeFromText()
        type = self.comboBoxType.currentText()
        date = self.dateEdit.text()
        time = self.comboBoxTime.currentText()
        print(date)
        self.close()

    def cancel(self):
        dialog = ConfirmMsgClass.ConfirmYesNo()
        if dialog.ans == True:
            print("Discard")
            self.close()
        else:
            print("Cancel")


def main():
    app = QApplication(sys.argv)
    win = newPatientDialog()
    win.exec_()


if __name__ == "__main__":
    main()
