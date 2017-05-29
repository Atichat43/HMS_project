class Date:
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0

    def setDate(self, date):
        self.day = date[0]
        self.month = date[1]
        self.year = date[2]

    def getDate(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)


class Appointment:
    #newAppointment = [0000, ["Type", "Date", "Time"], self.user, newPatient]
    #self.part_appointment, self.user, newPatient
    def __init__(self, case_id, appointment, doctor, patient):
        self.case_id = case_id
        self.type = ""
        self.date = Date()
        self.time = ""
        self.doctor = doctor
        self.patient = patient
        self.number_room = 0
        # "Type", "Date", "Time"
        self.setInfo(appointment[0], appointment[1], appointment[2])

    # BAR MANAGE PERSON DOCTOR
    def getData(self):
        text = []
        #Date Time Room PName Pre Plan
        text.append(self.case_id)
        text.append(self.date.getDate())
        text.append(self.time)
        text.append(self.number_room)
        text.append(self.patient.Name)
        # "Pre_OD", "Plan", "Underlying", "Treatment", "Note"
        text.append(self.patient.ExtraNote[0]) #Pre_OD
        text.append(self.patient.ExtraNote[1]) #Plan
        return text

    def getDataForCalendarDcotor(self):
        import Setting as s
        text = []
        text.append(self.time)
        text.append(str(self.number_room))
        text.append(self.patient.ExtraNote[1])
        text.append(self.patient.Name)
        text.append(str(s.Status.waiting.name))
        return text

    def getDataForRoomManager(self):
        text = []
        text.append(self.case_id)
        text.append(self.date.getDate())
        text.append(self.time)
        text.append(self.doctor.firstName)
        text.append(self.patient.Name)
        return text

    def setInfo(self, type, date, time):
        self.type = type
        self.date.setDate(date.split('/'))
        self.time = time

    def setRoom(self, number):
        self.number_room = number


