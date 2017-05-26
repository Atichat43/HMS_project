from Database import ControllerDatabase
import Setting as s


class AdminApplication(object):
    def __init__(self):
        self.ctrlDatabase = ControllerDatabase.ControllerDatabase(s.DB_USER)
        self.lst_admin = []
        self.lst_roommanager = []
        self.lst_doctor = []
        self.lst_nurse = []

    def getUserFromDatabase(self):
        obj_users = self.ctrlDatabase.loadObj()
        return obj_users

    def getListByPosition(self):
        users = self.getUserFromDatabase()
        for user in users:
            print(user)
            if user.getType() == s.Position.admin:
                self.lst_admin.append(user)
            elif user.getType() == s.Position.doctor:
                self.lst_doctor.append(user)
            elif user.getType() == s.Position.nurse:
                self.lst_nurse.append(user)
            elif user.getType() == s.Position.roommanager:
                self.lst_roommanager.append(user)
            else:
                print("Error")

    def getListAdmin(self):
        return self.lst_admin

    def getListDoctor(self):
        return self.lst_doctor

    def getListNurse(self):
        return self.lst_nurse

    def getListRoomManager(self):
        return self.lst_roommanager

if __name__ == "__main__":
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    win = AdminApplication()
    win.checkRegisteredUser(1, 1)
    exit(app.exec_())
