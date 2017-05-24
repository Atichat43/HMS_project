from PySide.QtCore import QEvent, Qt
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader

from Base.Dialog_MsgBox import ConfirmMsgClass
import Setting


class NewPatientDialog(QDialog):
    def __init__(self, parent=None):
        super(NewPatientDialog, self).__init__(parent)
        posX, posY, sizeW, sizeH = Setting.GEOMETRY_DIALOG_NEW_PATIENT
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.initUI()
        self.initLayout()
        self.initButton()
        self.initConnect()
        self.setDateEdit()

    def initUI(self):
        self.ui = QUiLoader().load('./View/Widget_NewPatientUI.ui', self)
        #self.comboBoxType = self.ui.findChild(QComboBox, "comboBox_type")
        self.dateEdit = self.ui.findChild(QDateEdit, "dateEdit")
        #self.comboBoxTime = self.ui.findChild(QComboBox, "comboBox_time")

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

    def initButton(self):
        pass

    def initConnect(self):
        pass

    def setDateEdit(self):
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(self)
        self.dateEdit.calendarWidget().setFirstDayOfWeek(Qt.Monday)

    def eventFilter(self, obj, event):
        if obj == self.dateEdit.calendarWidget() and event.type() == QEvent.Show:
            pos = self.dateEdit.mapToGlobal(self.dateEdit.geometry().bottomRight())
            self.dateEdit.calendarWidget().window().move(pos.x(), pos.y())
        return False

    def save(self):
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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = NewPatientDialog()
    win.show()
    win.exec_()
