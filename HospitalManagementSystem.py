from PySide.QtGui import *
import LoginUI
import Setting as s
from Employee.Admin import AdminUI as Admin
from Employee.Doctor import DoctorUI as Doctor
from Employee.Nurse import Nurse as Nurse
from Employee.Roommanager import RoomManagerUI as RoomManager


class HMS(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.initCentalWidget()
        self.mainWindow = QMainWindow()

    def initCentalWidget(self):
        posX, posY, sizeW, sizeH = s.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.login_widget = LoginUI.LoginWindow(self)
        self.central_widget.addWidget(self.login_widget)
        self.centralWidget().setCurrentWidget(self.login_widget)

    def loginSucess(self, user, position):
        if position == s.Position.admin:
            self.mainWindow = Admin.MainWindowAdmin(user)
        elif position == s.Position.doctor:
            self.mainWindow = Doctor.MainWindowDoctor(user)
        elif position == s.Position.nurse:
            self.mainWindow = Nurse.MainWindowNurse(user)
        elif position == s.Position.roommanager:
            self.mainWindow = RoomManager.MainWindowRoomManager(user)
        else:
            print("Error")
        self.appendCentral_widget(self.mainWindow)

    def appendCentral_widget(self, widget):
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
