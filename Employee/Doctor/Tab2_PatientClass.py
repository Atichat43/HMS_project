from PySide.QtGui import *
from Base.Widget_ManagePerson import Widget_ManagePersonClass
from Employee.Doctor.GuiClass import Dialog_NewPatientClass
from Patient import Dialog_HistoryReports
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
        self.tab2 = Widget_ManagePersonClass.WidgetManagePerson("Patient", self)
        self.b_view = self.tab2.b_edit
        self.b_view.setText("View History")
        patients = self.parent.crtlDatabase.getPatientFromDatabase()
        self.tab2.setSourceModel(s.HB_DOCTOR_PATIENT, patients)
        self.tab2.insertDeleteButton()

    def updateTable(self):
        patients = self.parent.crtlDatabase.getPatientFromDatabase()
        self.tab2.setSourceModel(s.HB_DOCTOR_PATIENT, patients)

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tab2)
        self.setLayout(layout)

    def initButton(self):
        self.b_view = self.tab2.b_edit
        self.b_newPatient = self.tab2.b_newPerson

    def initConnect(self):
        #self.b_view.clicked.connect(self.viewPatient)
        self.b_newPatient.clicked.connect(self.newPatient)

    """This func called By Widget_ManagePersonClass"""
    def editButtonPressed(self, AN):
        if AN is not None:
            self.viewHistoryReport(AN)
        else:
            print("is None")

    def deleteButtonPressed(self, id):
        self.parent.deleteButtonPressed(id)

    def newPatient(self):
        case_id = self.parent.getCurrentCaseID()
        dialog = Dialog_NewPatientClass.NewPatientDialog(self.user, case_id, self.parent)
        dialog.show()
        dialog.exec_()
        if dialog.returnVal:
            self.updateTable()
            self.parent.updateTable("Appointment")


    def viewHistoryReport(self, AN):
        report = self.parent.getHistoryReportByAN(AN)
        if report is not None:
            dialog = Dialog_HistoryReports.HistoryReportDialog(AN, report)
            dialog.exec_()
        else:
            dialog = QMessageBox()
            dialog.setText("Not Found")
            dialog.exec_()

