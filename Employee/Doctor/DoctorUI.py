from PySide.QtGui import QMainWindow, QGridLayout, QWidget, QTabWidget
from Employee.Doctor import Doctor, Tab1_CalendarClass, Tab2_PatientClass, Tab3_AppointmentClass
from Base.Dialog_MsgBox import ConfirmMsgClass
import Setting


class MainWindowDoctor(QMainWindow):
    def __init__(self, user, parent=None):
        QMainWindow.__init__(self, None)
        self.crtlDatabase = Doctor.DoctorApplication()
        self.parent = parent
        self.user = user
        self.initUI()
        self.initLayout()

    def initUI(self):
        posX, posY, sizeW, sizeH = Setting.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.setWindowTitle("Doctor window")
        self.setTab()
        self.show()

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tabWidget)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def setTab(self):
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet(Setting.SS_TabWidget)
        self.tab1 = Tab1_CalendarClass.Tab1Calendar(self.user, self)
        self.tab2 = Tab2_PatientClass.Tab2Patient(self.user, self)
        self.tab3 = Tab3_AppointmentClass.Tab3Appointment(self.user, self)
        self.tabWidget.addTab(self.tab1, "Dashboard")
        self.tabWidget.addTab(self.tab2, "Patient")
        self.tabWidget.addTab(self.tab3, "Appointment")

    def updateTable(self, tab):
        if tab == 'Appointment':
            self.tab3.updateTable()
        elif tab == 'Patient':
            self.tab2.updateTable()
        else:
            raise TypeError

    """-----------------------------DOCTOR APP---------------------------------------"""
    """-----PATIENT-----"""
    def getCurrentCaseID(self):
        return self.crtlDatabase.getCurrentCaseID()

    def addNewPatient(self, newPatient):
        self.crtlDatabase.addNewPatient(newPatient)

    def editPatient(self, oldPatient):
        self.crtlDatabase.editPatient(oldPatient)

    def patientValid(self, AN):
        return self.crtlDatabase.patientValid(AN)

    def oldPatientValid(self, AN, patient_name):
        return self.crtlDatabase.oldPatientValid(AN, patient_name)

    def deleteButtonPressed(self, AN):
        title = "Confirm deleting"
        text_info = "Delete this Patient"
        question = "Do you sure to delete " + str(AN)
        dialog = ConfirmMsgClass.ConfirmYesNo(title, text_info, question)
        if dialog.ans:
            patients = self.crtlDatabase.getPatientFromDatabase()
            appointments = self.crtlDatabase.getAppointmentFromDatabase()
            for patient in patients:
                if patient.AN == AN:
                    patients.remove(patient)
                    self.crtlDatabase.updatePatientDatabase(patients)
                    self.tab2.updateTable()
                    break
            for appointment in appointments:
                if appointment.patient.AN == AN:
                    appointments.remove(appointment)
                    self.crtlDatabase.updateAppointmentDatabase(appointments)
                    self.tab3.updateTable()
                    break
        else:
            pass

    """-----APPOINTMENT----"""
    def getAppointment(self):
        return self.crtlDatabase.getAppointmentByDoctor(self.user.id)

    def addNewAppointment(self, newAppointment):
        self.crtlDatabase.addNewAppointment(newAppointment)

    def appointmentValid(self, date, time, doctor):
        return self.crtlDatabase.appointmentValid(date, time, doctor)

    def getPatientByCaseId(self, case_id):
        return self.crtlDatabase.getPatientByCaseId(case_id, self.user.id)

    def getAppointmentByAN(self, AN):
        return self.crtlDatabase.getAppointmentByAN(AN)

    def getHistoryReportByAN(self, AN):
        return self.crtlDatabase.getHistoryReportByAN(AN)


