from PySide.QtGui import QMainWindow, QGridLayout, QWidget, QTabWidget
from Employee.Doctor import Doctor, Tab1_CalendarClass, Tab2_PatientClass, Tab3_AppointmentClass
import Setting


class MainWindowDoctor(QMainWindow):
    def __init__(self, user, parent=None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.user = user
        self.crtlDatabase = Doctor.DoctorApplication()
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

    def addNewPatient(self, newPatient):
        self.crtlDatabase.addNewPatient(newPatient)

    def addNewAppointment(self, newAppointment):
        self.crtlDatabase.addNewAppointment(newAppointment)

    def getCurrentCaseID(self):
        return self.crtlDatabase.getCurrentCaseID()

    def getAppointment(self):
        print("in get Appointment")
        print(self.user.id)
        return self.crtlDatabase.getAppointmentByDoctor(self.user.id)

    def appointmentValid(self, date, time, doctor):
        return self.crtlDatabase.appointmentValid(date, time, doctor)

    def patientValid(self, AN):
        return self.crtlDatabase.patientValid(AN)


if __name__ == "__main__":
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    user = object
    win = MainWindowDoctor(user)
    exit(app.exec_())
