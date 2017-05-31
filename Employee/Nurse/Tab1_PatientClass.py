from PySide.QtGui import *
from Base.Widget_ManagePerson import Widget_ManagePersonClass
from Employee.Doctor.GuiClass import Dialog_3ReportPatientClass
import Setting as s

class Tab1Patient(QWidget):
    def __init__(self, user, parent=None):
        QWidget.__init__(self, None)
        self.user = user
        self.parent = parent
        self.initUI()
        self.initLayout()
        self.initButton()

    def initUI(self):
        self.tab1 = Widget_ManagePersonClass.WidgetManagePerson("Patient", self)
        patients = self.parent.nurse_app.getPatientFromDatabase()
        self.tab1.setSourceModel(s.HB_DOCTOR_PATIENT, patients)

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tab1)
        self.setLayout(layout)

    def initButton(self):
        self.b_edit = self.tab1.b_edit
        self.b_newPatient = self.tab1.b_newPerson
        self.b_newPatient.setEnabled(False)
        self.b_newPatient.setVisible(True)

    def updateTable(self):
        patients = self.parent.nurse_app.getPatientFromDatabase()
        self.tab1.setSourceModel(s.HB_DOCTOR_PATIENT, patients)

    """This func called By Widget_ManagePersonClass"""
    def editButtonPressed(self, AN):
        if AN is not None:
            self.edit3Report(AN)
        else:
            print("is None")
            raise KeyError

    def edit3Report(self, AN):
        patient = self.parent.getPatientByAN(AN)
        appointment = self.parent.getAppointmentByAN(AN)
        if patient is not None:
            if appointment is not None:
                dialog = Dialog_3ReportPatientClass.ReportPatient(AN, patient, appointment, self.parent)
                dialog.show()
                dialog.exec_()
            else:
                error = QErrorMessage()
                error.showMessage("Not found Appointment")
                error.setWindowTitle("Error!!!")
                error.exec_()
        else:
            error = QErrorMessage()
            error.showMessage("Invalid AN")
            error.setWindowTitle("Error!!!")
            error.exec_()

    def createHistory(self, h):
        self.parent.createHistory(h)
