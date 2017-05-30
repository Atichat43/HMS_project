from PySide.QtGui import QMainWindow, QGridLayout, QWidget, QTabWidget
from Employee.Nurse import Tab1_PatientClass, Nurse
import Setting

class MainWindowNurse(QMainWindow):
    def __init__(self, user, parent=None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.user = user
        self.crtlDatabase = Nurse.NurseApplication()
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
        return self.crtlDatabase.getPatientByAN(AN)

    def getAppointmentByAN(self, AN):
        return self.crtlDatabase.getAppointmentByAN(AN)

    def updatePatient(self, patient):
        return self.crtlDatabase.editPatient(patient)

    def createHistory(self, new_history_report):
        self.crtlDatabase.createHistory(new_history_report)
