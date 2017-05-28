from PySide.QtGui import *
from Base.Widget_ManagePerson import Widget_ManagePersonClass
from Employee.Doctor.GuiClass import Dialog_3ReportPatientClass, Dialog_NewPatientClass
import Setting as s

class Tab3Appointment(QWidget):
    def __init__(self, user, parent=None):
        QWidget.__init__(self, None)
        self.user = user
        self.parent = parent
        self.initUI()
        self.initLayout()
        self.initButton()
        self.initConnect()

    def initUI(self):
        self.tab3 = Widget_ManagePersonClass.WidgetManagePerson("Appointment", self)
        appointments = self.parent.crtlDatabase.getAppointmentByDoctor(self.user.id)
        self.tab3.setSourceModel(s.HEAD_BAR_PATIENT, appointments)

    def updateTable(self):
        appointments = self.parent.crtlDatabase.getAppointmentFromDatabase()
        self.tab2.setSourceModel(s.HEAD_BAR_PATIENT, appointments)

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tab3)
        self.setLayout(layout)

    def initButton(self):
        self.b_view = self.tab3.b_edit
        self.b_newPatient = self.tab3.b_newPerson

    def initConnect(self):
        self.b_newPatient.clicked.connect(self.newPatient)

    def editButtonPressed(self, case_id):
        if case_id is not None:
            self.viewPatient(case_id)
        else:
            print("is None")

    def viewPatient(self, case_id):
        print(case_id)
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
    tab2_widget = Tab3Appointment()
    sys.exit(app.exec_())
