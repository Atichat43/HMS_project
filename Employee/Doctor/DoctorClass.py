from Employee import EmployeeClass
import Setting as s

class Doctor(EmployeeClass.Employee):
    def __init__(self, id, username, password, firstname, lastname, phone_number, department):
        EmployeeClass.Employee.__init__(self, id, username, password, s.Position.doctor, firstname, lastname, phone_number)
        self.department = department

    def setDepartment(self, new_department):
        self.department = new_department

    def getDepartment(self):
        return self.department
    
