from Database import ControllerDatabase
from Base.Dialog_MsgBox import ConfirmMsgClass
import Setting as s


class LoginSystem(object):
    def __init__(self):
        self.ctrlDatabase = ControllerDatabase.ContorllerDatabase(s.DB_USER)

    def getUserFromDatabase(self):
        obj_users = self.ctrlDatabase.loadObj()
        return obj_users

    def checkRegisteredUser(self, userName, password):
        users = self.getUserFromDatabase()
        for user in users:
            if (userName == user.getUserName() and
                        password == user.getPsw()):
                return 1, user
        dialog = ConfirmMsgClass.ConfirmYesNo()
        dialog.show()
        dialog.exec_()
        return 0, None


if __name__ == "__main__":
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    win = LoginSystem()
    win.checkRegisteredUser(1, 1)
    exit(app.exec_())
