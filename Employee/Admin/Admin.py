from Database import ControllerDatabase
from Employee.Doctor import DoctorClass as doctor
from Employee.Nurse import NurseClass as nurse
from Employee.Admin import AdminClass as admin
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
        self.lst_doctor.clear()
        self.lst_roommanager.clear()
        self.lst_nurse.clear()
        self.lst_admin.clear()
        users = self.getUserFromDatabase()
        for user in users:
            if user.getType() == s.Position.admin:
                self.lst_admin.append(user)
            elif user.getType() == s.Position.doctor:
                self.lst_doctor.append(user)
            elif user.getType() == s.Position.nurse:
                self.lst_nurse.append(user)
            elif user.getType() == s.Position.roommanager:
                self.lst_roommanager.append(user)
            else:
                print("NOT FOUND TYPE EMPLOYEE")
                raise TypeError

    def getListAdmin(self):
        return self.lst_admin

    def getListDoctor(self):
        return self.lst_doctor

    def getListNurse(self):
        return self.lst_nurse

    def getListRoomManager(self):
        return self.lst_roommanager

    def getNewIDByUserType(self, position):
        print("get new id by " + str(position))
        if position == s.Position.admin.name:
            admins = self.getListAdmin()
            new_id = str("A00" + str(int(admins[-1].id[-1])+1))
            return new_id
        elif position == s.Position.nurse.name:
            nurses = self.getListNurse()
            new_id = str("N00" + str(int(nurses[-1].id[-1]) + 1))
            return new_id
        elif position == s.Position.doctor.name:
            doctors = self.getListAdmin()
            new_id = str("D00" + str(int(doctors[-1].id[-1]) + 1))
            return new_id
        else:
            print("NOT FOUND TYPE EMPLOYEE")
            raise TypeError

    def updateDatabase(self, all_user):
        self.ctrlDatabase.updateObject(all_user)

    def editEmployee(self, id, data, position):
        users = self.getUserFromDatabase()
        for i in range(len(users)):
            if users[i].id == id:
                if users[i].username == data[2]: #old username
                    print("---Update" + str(users[i].id) + "  old username---")
                    users[i] = self.newEmployee(data, position)
                    self.ctrlDatabase.updateObject(users)
                    return True

                elif self.userNameValid(data[1]):
                    print("---Update" + str(users[i].id) + "  new username---")
                    users[i] = self.newEmployee(data, position)
                    self.ctrlDatabase.updateObject(users)
                    return True

                else:
                    print("INVALID USERNAME")
                    return False

        print("!!!---NOT FOUND THIS ID---!!!")
        return False

    def newEmployee(self, data, position):
        #[id, username, psw, firstName, lastName, phone]
        if position == s.Position.doctor.name:
            return doctor.Doctor(data[0], data[1], data[2], data[4], data[5], data[6])
        elif position == s.Position.nurse.name:
            return nurse.Nurse(data[0], data[1], data[2], data[4], data[5], data[6])
        elif position == s.Position.admin.name:
            return admin.Admin(data[0], data[1], data[2], data[4], data[5], data[6])
        else:
            raise TypeError

    def addNewEmployee(self, data, position):
        if self.idValid(data[0]) and self.userNameValid(data[1]):
            users = self.getUserFromDatabase()
            newEmployee = self.newEmployee(data, position)
            users.append(newEmployee)
            self.ctrlDatabase.updateObject(users)
            return True
        else:
            print("ID or/and Username is/are invalid")
            return False

    def userNameValid(self, userName):
        users = self.getUserFromDatabase()
        for user in users:
            if user.username == userName:
                return False
        return True

    def idValid(self, id):
        users = self.getUserFromDatabase()
        for user in users:
            if user.id == id:
                return False
        return True


