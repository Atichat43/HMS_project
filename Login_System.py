from Database import ControllerDatabase
import Setting as s

class LoginSystem(object):
    def __init__(self):
        self.ctrlDatabase = ControllerDatabase.ControllerDatabase(s.DB_USER)

    def getUserFromDatabase(self):
        obj_users = self.ctrlDatabase.loadObj()
        return obj_users

    def checkRegisteredUser(self, userName, password):
        users = self.getUserFromDatabase()
        for user in users:
            if (userName == user.getUsername() and
                        password == user.getPassword()):
                return 1, user, user.getType()
        return 0, None, None
