from Roommaneger import setting


class Room:
    def __init__(self, num, status):
        self.number = num
        self.color = setting.STATUS[status]
        self.allPatient = []

    def changeStatus(self, status):
        self.color = status

    def addPatient(self, patient):
        self.allPatient.append(patient)
