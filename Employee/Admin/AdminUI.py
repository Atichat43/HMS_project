from PySide.QtGui import *
from Base.Widget_ManagePerson import Widget_ManagePersonClass
from Employee.Admin import Admin
import Setting as s


class MainWindowAdmin(QMainWindow):
    def __init__(self, user):
        super(MainWindowAdmin, self).__init__()
        self.ctrlDatabase = Admin.AdminApplication()
        self.initUI()
        self.initLayout()
        self.user = user
        self.allRowDatabaseDoctor = []
        self.allRowDatabaseNurse = []
        self.allRowDatabaseRoom = []

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
        self.tab1 = Widget_ManagePersonClass.WidgetManagePerson("Doctor")
        self.tab1.setSourceModel(s.HEAD_BAR_DOCTOR, self.allRowDatabaseDoctor)
        self.tab2 = Widget_ManagePersonClass.WidgetManagePerson("Nurse")
        self.tab2.setSourceModel(s.HEAD_BAR_NURSE, self.allRowDatabaseNurse)
        self.tab3 = Widget_ManagePersonClass.WidgetManagePerson("Room manager")
        self.tab3.setSourceModel(s.HEAD_BAR_ROOMMANAGER, self.allRowDatabaseRoom)
        self.tabWidget.addTab(self.tab1, "Doctor")
        self.tabWidget.addTab(self.tab2, "Nurse")
        self.tabWidget.addTab(self.tab3, "RoomManager")

    def updateDatabase(self):
        self.ctrlDatabase.getListByPosition()
        self.allRowDatabaseDoctor = self.ctrlDatabase.getListDoctor()
        self.allRowDatabaseNurse = self.ctrlDatabase.getListNurse()
        self.allRowDatabaseRoom = self.ctrlDatabase.getListRoomManager()


