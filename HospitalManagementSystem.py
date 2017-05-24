from PySide.QtGui import *
import Login
import Setting as s
from Employee.Admin import Admin as Admin
from Employee.Doctor import Doctor as Doctor
from Employee.Nurse import Nurse as Nurse
from Employee.Roommanager import RoomManager as RoomManager


class HMS(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.initCentalWidget()

    def initCentalWidget(self):
        self.login_widget = Login.LoginWindow(self)
        self.central_widget.addWidget(self.login_widget)
        self.centralWidget().setCurrentWidget(self.login_widget)

    def loginSucess(self, position):
        if position == s.Position.admin.value:
            mainWindow = Admin.MainWindowAdmin()
        elif position == s.Position.doctor.value:
            mainWindow = Doctor.MainWindowDoctor()
        elif position == s.Position.nurse.value:
            mainWindow = Nurse.MainWindowNurse()
        elif position == s.Position.roomManager.value:
            mainWindow = RoomManager.MainWindowRoomManager()
        else:
            print("Error")
        self.appendCental_widget(mainWindow)

    def appendCental_widget(self, widget):
        self.mainWindow = widget
        self.central_widget.addWidget(self.mainWindow)
        self.centralWidget().setCurrentWidget(self.mainWindow)


def main():
    from PySide.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)
    window = HMS()
    window.show()
    exit(app.exec_())

main()
