from PySide.QtGui import *
from Base.Widget_ManagePerson import Widget_ManagePersonClass
from Base.Dialog_MsgBox import ConfirmMsgClass
from Employee.Admin import Admin
import Employee.Admin.Dialog_NewEmployeeClass as d
import Setting as s


class MainWindowAdmin(QMainWindow):
    def __init__(self, user):
        super(MainWindowAdmin, self).__init__()
        self.admin_app = Admin.AdminApplication()
        self.user = user
        self.all_user = []
        self.initUI()
        self.initLayout()
        self.initButton()

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
        self.tab1.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[s.UserPosition.doctor.value])
        self.tab2 = Widget_ManagePersonClass.WidgetManagePerson("Nurse", self)
        self.tab2.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[s.UserPosition.nurse.value])
        self.tab3 = Widget_ManagePersonClass.WidgetManagePerson("Admin", self)
        self.tab3.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[s.UserPosition.admin.value])
        self.tabWidget.addTab(self.tab1, "Doctor")
        self.tabWidget.addTab(self.tab2, "Nurse")
        self.tabWidget.addTab(self.tab3, "Admin")

    def initButton(self):
        #init new Employee
        self.b_newDoctor = self.tab1.b_newPerson
        self.b_newDoctor.clicked.connect(lambda: self.newEmployee(s.UserPosition.doctor.name))
        self.b_newNurse = self.tab2.b_newPerson
        self.b_newNurse.clicked.connect(lambda: self.newEmployee(s.UserPosition.nurse.name))
        self.b_newAdmin = self.tab3.b_newPerson
        self.b_newAdmin.clicked.connect(lambda: self.newEmployee(s.UserPosition.admin.name))

        #init delete Employee
        self.tab1.insertDeleteButton()
        self.tab2.insertDeleteButton()
        self.tab3.insertDeleteButton()

    def updateDatabase(self):
        self.admin_app.getListByPosition()
        self.all_user = []
        self.all_user.append(self.admin_app.getListDoctor())
        self.all_user.append(self.admin_app.getListNurse())
        self.all_user.append(self.admin_app.getListAdmin())

    def updateTable(self, type):
        self.updateDatabase()
        if type == s.UserPosition.doctor.name:
            print("Update Table: " + str(type))
            self.all_user[s.UserPosition.doctor.value] = self.admin_app.getListDoctor()
            self.tab1.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[s.UserPosition.doctor.value])
        elif type == s.UserPosition.nurse.name:
            print("Update Table: " + str(type))
            self.all_user[s.UserPosition.nurse.value] = self.admin_app.getListNurse()
            self.tab2.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[s.UserPosition.nurse.value])
        elif type == s.UserPosition.admin.name:
            print("Update Table: " + str(type))
            self.all_user[s.UserPosition.admin.value] = self.admin_app.getListAdmin()
            self.tab3.setSourceModel(s.HEAD_BAR_ADMIN, self.all_user[s.UserPosition.admin.value])
        else:
            raise TypeError

    def getListUserByType(self, type):
        if type == "D":
            return s.UserPosition.doctor.value
        elif type == "N":
            return s.UserPosition.nurse.value
        elif type == "A":
            return s.UserPosition.admin.value
        else:
            raise ValueError

    def getPositionByPosition(self, position):
        if position == "D":
            return s.UserPosition.doctor.name
        elif position == "N":
            return s.UserPosition.nurse.name
        elif position == "A":
            return s.UserPosition.admin.name
        else:
            raise ValueError

    def editButtonPressed(self, id):
        position = self.getListUserByType(id[:1])
        for i in range(len(self.all_user[position])):
            if id == self.all_user[position][i].id:
                dialog = d.EditOrNewEmployeeDialog("edit", id, self)
                dialog.show()
                dialog.exec_()

    def deleteButtonPressed(self, id):
        title = "Confirm deleting"
        textInfo = "Delete this Employee"
        question = "Do you sure to delete " + str(id)
        dialog = ConfirmMsgClass.ConfirmYesNo(title, textInfo, question)
        if dialog.ans == True:
            users = self.admin_app.getUserFromDatabase()
            for user in users:
                if user.id == id:
                    users.remove(user)
                    position = self.getPositionByPosition(id[:1])
                    self.admin_app.updateDatabase(users)
                    self.updateTable(position)
                    return True
            raise KeyError
        else:
            pass

    def editEmployee(self, id, data, position):
        if self.admin_app.editEmployee(id, data, position):
            self.updateTable(position)
            return True
        return False

    def newEmployee(self, position):
        dialog = d.EditOrNewEmployeeDialog("new", position, self)
        dialog.show()
        dialog.exec_()

    def addNewEmployee(self, data, position):
        if self.admin_app.addNewEmployee(data, position):
            self.updateTable(position)
            return True
        return False

    def getNewIDByUserType(self, position):
        return self.admin_app.getNewIDByUserType(position)




