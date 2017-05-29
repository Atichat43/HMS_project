from PySide.QtGui import *
from Base.Widget_ManagePerson import Widget_ManagePersonClass
from Employee.Admin import Admin
import Employee.Admin.Dialog_editOrNewEmployeeClass as d
import Setting as s

from enum import Enum
class UserPosition(Enum):
    doctor = 0
    nurse = 1
    admin = 2

class MainWindowAdmin(QMainWindow):
    def __init__(self, user):
        super(MainWindowAdmin, self).__init__()
        self.ctrlDatabase = Admin.AdminApplication()
        self.initUI()
        self.initLayout()
        self.user = user
        self.all_user = []
        # self.allRowDatabaseDoctor = []
        # self.allRowDatabaseNurse = []
        # self.allRowDatabaseAdmin = []

    def initUI(self):
        posX, posY, sizeW, sizeH = s.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.setWindowTitle("Admin Main Window")
        self.setTab()
        self.show()

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tabWidget)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def setTab(self):
        self.updateDatabase()
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet(s.SS_TabWidget)
        self.tab1 = Widget_ManagePersonClass.WidgetManagePerson("Doctor", self)
        self.tab1.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[UserPosition.doctor.value])
        self.tab2 = Widget_ManagePersonClass.WidgetManagePerson("Nurse", self)
        self.tab2.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[UserPosition.nurse.value])
        self.tab3 = Widget_ManagePersonClass.WidgetManagePerson("Admin", self)
        self.tab3.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[UserPosition.admin.value])
        self.tabWidget.addTab(self.tab1, "Doctor")
        self.tabWidget.addTab(self.tab2, "Nurse")
        self.tabWidget.addTab(self.tab3, "Admin")

    def updateDatabase(self):
        self.ctrlDatabase.getListByPosition()
        self.all_user.append(self.ctrlDatabase.getListDoctor())
        self.all_user.append(self.ctrlDatabase.getListNurse())
        self.all_user.append(self.ctrlDatabase.getListAdmin())

    def getListUserByType(self, type):
        if type == "D":
            return UserPosition.doctor.value
        elif type == "N":
            return UserPosition.nurse.value
        elif type == "A":
            return UserPosition.admin.value
        else:
            raise ValueError

    def editButtonPressed(self, id):
        self.updateDatabase()
        position = self.getListUserByType(id[:1])
        print(position)
        for i in range(len(self.all_user[position])):
            pass




