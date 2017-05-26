from Employee import EmployeeClass
import Setting as s

class Nurse(EmployeeClass.Employee):
    def __init__(self, id, username, password, firstname, lastname, phone_number):
        EmployeeClass.Employee.__init__(self, id, username, password, s.Position.nurse, firstname, lastname, phone_number)

