from Appointment import AppointmentClass


class PreReportByDoctor:
    def __init__(self, type):
        self.opd = 0
        self.type = type
        self.appointment = AppointmentClass
        self.preDiagonsis = ""
        self.operationPlan = ""
        self.underlying = ""
        self.specialTreament = ""
        self.note = ""

    def setOpd(self, boo):
        self.opd = boo

    def setDoc(self, preDiagonsis, operationPlan, underlying, specialTreament, note):
        self.preDiagonsis = preDiagonsis
        self.operationPlan = operationPlan
        self.underlying = underlying
        self.specialTreament = specialTreament
        self.note = note

    def getDoc(self):
        return [self.preDiagonsis, self.operationPlan, self.underlying, self.specialTreament, self.note]


"""----------------------------BY NURSE---------------------"""

class PreReportByNurse(object):
    def __init__(self, premed, PRC, FFP, Plt, PC, plannedICU, BedNO, service, ASA, BW, HT, BP, P, RR, T, GCS,
                 smoking, alcoholic, allergy,lt=[]):
        self.premed = premed
        self.BLprepared = [PRC, FFP, Plt, PC]  ## PRC, FFP, PLT, PC int
        self.plannedICU = plannedICU  ## boolean
        self.BedNO = BedNO  ## int
        self.service = service  ## string ('in', 'out')
        self.ASA = ASA  ## string
        self.BW = int(BW)  ## int
        self.HT = int(HT)  ## int
        self.BMI = self.BW / (self.HT ** 2)
        self.BP = BP  ## int
        self.P = P  ## int
        self.RR = RR  ## int
        self.T = T  ## int
        self.GCS = GCS  ## string and int[('E','M','V')
        self.smoking = smoking  ## boolean
        self.alcoholic = alcoholic  ## boolean
        self.allergy = allergy  ## string
        self.allergy_list = [] ##list
        if self.allergy == "Yes":
            for i in lt:
                if i[0] != "":
                    self.allergy_list.append(i)


    def setpremed(self, new_premed):
        self.premed = new_premed

    def getpremed(self):
        return self.premed

    def setBLprepared(self, new_PRC, new_FFP, new_Plt, new_PC):
        self.BLprepared = [new_PRC, new_FFP, new_Plt, new_PC]

    def getBLprepared(self):
        return self.BLprepared

    def setplannedICU(self, new_plannedICU):
        self.plannedICU = new_plannedICU

    def getplannedICU(self):
        return self.plannedICU

    def setfullBed(self, new_fullBed):
        self.fullBed = new_fullBed

    def getfullBed(self):
        return self.fullBed

    def setservice(self, new_service):
        self.service = new_service

    def setservice(self):
        return self.service

    def setASA(self, new_ASA):
        self.ASA = new_ASA

    def getASA(self):
        return self.ASA

    def setBMI(self, new_BW, new_HT):
        self.BW = new_BW
        self.HT = new_HT
        self.BMI = self.BW / (self.HT ** 2)

    def getBMI(self):
        return [self.BW, self.HT, self.BMI]

    def setMeasure(self, new_BP, new_P, new_RR, new_T):
        self.BP = new_BP
        self.P = new_P
        self.RR = new_RR
        self.T = new_T

    def getMeasure(self):
        return [self.BP, self.P, self.RR, self.T]

    def setGCS(self, new_GCS1, new_GCS2):
        self.GCS = [new_GCS1, new_GCS2]

    def getGCS(self):
        return self.GCS

    def setAddicted(self, new_smoking, new_alcoholic):
        self.smoking = new_smoking
        self.alcoholic = new_alcoholic

    def getAddicted(self):
        return [self.smoking, self.alcoholic]

    def setAllergy(self, new_allergy):
        self.allergy = new_allergy

    def getAllergy(self):
        return self.allergy

    def getData(self):
        data = []
        dataBox = []
        data.append(self.premed)
        for i in self.BLprepared:
            data.append(i)
        dataBox.append(self.plannedICU)
        data.append(self.BedNO)
        dataBox.append(self.service)
        dataBox.append(self.ASA)
        data.append(str(self.BW))
        data.append(str(self.HT))
        data.append(str(self.BMI))
        data.append(str(self.BP))
        data.append(str(self.P))
        data.append(str(self.RR))
        data.append(str(self.T))
        dataBox.append(str(self.GCS))
        dataBox.append(self.smoking)
        dataBox.append(self.alcoholic)
        dataBox.append(self.allergy)
        if self.allergy == "Yes":
            for i in self.allergy_list:
                data.append(i)
        else:
            for i in range(6):
                data.append('-')
        return data, dataBox