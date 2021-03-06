from PySide.QtGui import QMainWindow, QGridLayout, QWidget, QTabWidget
from Employee.Nurse import Tab1_PatientClass, Nurse
from Base.Dialog_MsgBox import ConfirmMsgClass
import Setting


class MainWindowNurse(QMainWindow):
    def __init__(self, user, parent=None):
        QMainWindow.__init__(self, None)
        self.nurse_app = Nurse.NurseApplication()
        self.parent = parent
        self.user = user
        self.initUI()
        self.initLayout()

    def initUI(self):
        posX, posY, sizeW, sizeH = Setting.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.setWindowTitle("Nurse window")
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
        self.tab1 = Tab1_PatientClass.Tab1Patient(self.user, self)
        self.tabWidget.addTab(self.tab1, "Patient")

    def getPatientByAN(self, AN):
        return self.nurse_app.getPatientByAN(AN)

    def getAppointmentByAN(self, AN):
        return self.nurse_app.getAppointmentByAN(AN)

    def deleteButtonPressed(self, AN):
        title = "Confirm deleting"
        text_info = "Delete this Patient"
        question = "Do you sure to delete " + str(AN)
        dialog = ConfirmMsgClass.ConfirmYesNo(title, text_info, question)
        if dialog.ans:
            patients = self.nurse_app.getPatientFromDatabase()
            appointments = self.nurse_app.getAppointmentFromDatabase()
            for patient in patients:
                if patient.AN == AN:
                    patients.remove(patient)
                    self.nurse_app.updatePatientDatabase(patients)
                    self.tab1.updateTable()
                    break
            for appointment in appointments:
                if appointment.patient.AN == AN:
                    appointments.remove(appointment)
                    self.nurse_app.updateAppointmentDatabase(appointments)
                    break
        else:
            pass

    def updatePatient(self, patient):
        return self.nurse_app.editPatient(patient)

    def createHistory(self, new_history_report):
        self.nurse_app.createHistory(new_history_report)
