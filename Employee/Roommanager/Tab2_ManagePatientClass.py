from PySide.QtCore import Qt
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
from Base.Widget_ManagePerson import Widget_ManagePersonClass
from Employee.Roommanager import Widget_ManageAppointmentClass
import Setting as s

class Tab2ManagePatient(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,None)
        self.parent = parent
        self.initUI()
        self.initLayout()
        self.initButton()
        self.initConnect()

    # def initUI(self):
    #     self.tab2 = Widget_ManagePersonClass.WidgetManagePerson("Patient", self)
    #     appointments = self.parent.crtlDatabase.getAppointmentByDoctor(self.user.id)
    #     self.tab2.setSourceModel(s.HEAD_BAR_PATIENT, appointments)

    def initUI(self):
        self.tab2 = Widget_ManageAppointmentClass.WidgetManageAppointment("Patient")
        appointments = self.parent.crtlDa
        self.tab2.setSourceModel(s.HEAD_BAR_PATIENT, allRow)


    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tab2)
        self.setLayout(layout)

    def initButton(self):
        self.b_view = self.tab2.b_edit
        self.b_newEMCase = self.tab2.b_newPerson
        self.b_newEMCase.setText("new EM Case")
        self.b_newEMCase.setAutoFillBackground(True)
        self.b_newEMCase.setStyleSheet(Setting.SS_Button_EMCASE)

    def initConnect(self):
        self.b_view.clicked.connect(self.viewPatient)
        self.b_newEMCase.clicked.connect(self.newEMCase)

    def viewPatient(self):
        pass
        # dialog = Dialog_3ReportPatientClass.ReportPatient()
        # dialog.show()
        # dialog.exec_()

    def newEMCase(self):
        pass
        # dialog = Dialog_NewPatientClass.NewPatientDialog()
        # dialog.show()
        # dialog.exec_()


if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication

    app = QApplication(sys.argv)
    tab2_widget = Tab2ManagePatient()
    tab2_widget.show()
    sys.exit(app.exec_())
