class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


class Time:
    def __init__(self):
        pass

class Appointment:
    def __init__(self):
        self.date = Date(0, 0, 0)
        self.time = Time
        self.Nroom = 0
        self.Dname = ""
        self.Pname = ""

    def setDate(self, day, month, year):
        self.date = Date(day, month, year)

    def getDate(self):
        return self.date

    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time


