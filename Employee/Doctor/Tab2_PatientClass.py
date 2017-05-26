from PySide.QtGui import *
from Base.Widget_ManagePerson import Widget_ManagePersonClass
from Employee.Doctor.GuiClass import Dialog_3ReportPatientClass, Dialog_NewPatientClass
import Setting as s

class Tab2Patient(QWidget):
    def __init__(self, user, parent=None):
        QWidget.__init__(self, None)
        self.user = user
        self.parent = parent
        self.initUI()
        self.initLayout()
        self.initButton()
        self.initConnect()

    def initUI(self):
        self.tab2 = Widget_ManagePersonClass.WidgetManagePerson("Patient")
        patients = self.parent.crtlDatabase.getPatientFromDatabase()
        self.tab2.setSourceModel(s.HEAD_BAR_PATIENT, patients)

    def updateTable(self):
        patients = self.parent.crtlDatabase.getPatientFromDatabase()
        self.tab2.setSourceModel(s.HEAD_BAR_PATIENT, patients)

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tab2)
        self.setLayout(layout)

    def initButton(self):
        self.b_view = self.tab2.b_edit
        self.b_newPatient = self.tab2.b_newPerson

    def initConnect(self):
        self.b_view.clicked.connect(self.viewPatient)
        self.b_newPatient.clicked.connect(self.newPatient)

    def viewPatient(self):
        dialog = Dialog_3ReportPatientClass.ReportPatient()
        dialog.show()
        dialog.exec_()

    def newPatient(self):
        case_id = self.parent.getCurrentCaseID()
        dialog = Dialog_NewPatientClass.NewPatientDialog(self.user, case_id, self.parent)
        dialog.show()
        dialog.exec_()
        self.updateTable()


if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    tab2_widget = Tab2Patient()
    sys.exit(app.exec_())
