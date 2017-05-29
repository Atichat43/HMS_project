class PostReportPatient(object):
    def __init__(self):
        #self.num = num
        self.Attempt = []
        #self.result = result
        self.Anesthetic_complications_operationroom = []
        self.Anesthetic_complications_admitroom = []
        self.Anesthetic_complications_admitroom_2hrs = []
        self.Anesthetic_complications_admitroom_24hrs = []
        self.Anesthetic_complications_procedure = []
        self.Anesthetic_complications_admitroom_48hrs = []
        self.Anesthetic_complications_admitroom_7day = []

    # def setresult(self, new_result):
    #     self.result = new_result
    #
    # def getresult(self):
    #     return self.result

    def addAttempt(self, new_date, new_AnestheticNurse):
        self.Attempt.append((new_date, new_AnestheticNurse))

    def getAttempt(self):
        return self.Attempt

    def setAnesthetic_complications_operationroom(self, new_Anesthetic_complications_operationroom):
        self.Anesthetic_complications_operationroom = new_Anesthetic_complications_operationroom

    def getAnesthetic_complications_operationroom(self):
        return self.Anesthetic_complications_operationroom

    def setAnesthetic_complications_admitroom(self, new_Anesthetic_complications_admitroom):
        self.Anesthetic_complications_admitroom = new_Anesthetic_complications_admitroom

    def getAnesthetic_complications_admitroom(self):
        return self.Anesthetic_complications_admitroom

    def setAnesthetic_complications_admitroom_2hrs(self, new_Anesthetic_complications_admitroom_2hrs):
        self.Anesthetic_complications_admitroom_2hrs = new_Anesthetic_complications_admitroom_2hrs

    def getAnesthetic_complications_admitroom_2hrs(self):
        return self.Anesthetic_complications_admitroom_2hrs

    def setAnesthetic_complications_admitroom_24hrs(self, new_Anesthetic_complications_admitroom_24hrs):
        self.Anesthetic_complications_admitroom_24hrs = new_Anesthetic_complications_admitroom_24hrs

    def getAnesthetic_complications_admitroom_24hrs(self):
        return self.Anesthetic_complications_admitroom_24hrs

    def setAnesthetic_complications_procedure(self, new_Anesthetic_complications_procedure):
        self.Anesthetic_complications_procedure = new_Anesthetic_complications_procedure

    def getAnesthetic_complications_procedure(self):
        return self.Anesthetic_complications_procedure

    def setAnesthetic_complications_admitroom_48hrs(self, new_Anesthetic_complications_admitroom_48hrs):
        self.Anesthetic_complications_admitroom_48hrs = new_Anesthetic_complications_admitroom_48hrs

    def getAnesthetic_complications_admitroom_48hrs(self):
        return self.Anesthetic_complications_admitroom_48hrs

    def setAnesthetic_complications_admitroom_7day(self, new_Anesthetic_complications_admitroom_7day):
        self.Anesthetic_complications_admitroom_7day = new_Anesthetic_complications_admitroom_7day

    def getAnesthetic_complications_admitroom_7day(self):
        return self.Anesthetic_complications_admitroom_7day

    def getData(self):
        data = []
        data.append(self.Anesthetic_complications_operationroom)
        data.append(self.Anesthetic_complications_admitroom)
        data.append(self.Anesthetic_complications_admitroom_2hrs)
        data.append(self.Anesthetic_complications_admitroom_24hrs)
        data.append(self.Anesthetic_complications_procedure)
        data.append(self.Anesthetic_complications_admitroom_48hrs)
        data.append(self.Anesthetic_complications_admitroom_7day)
        return data

