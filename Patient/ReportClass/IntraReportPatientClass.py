import time
class IntraReportPatient():
    def __init__(self, num_case_year, num_case_month, room, building, evaluation, Pre_evaluateNurse, AN, patientName, age_hour, age_day, age_month, age_year,
                 arrivePlace, departPlace, typeofOperation, department, service, ASA, Dormicum, Ephedrine, Ketamine, Anesthesia_technique, Combined_technique, airwayManagement,
                 Anesthesia_start_time, Anesthesia_finish_time, Anesthesia_time, Anesthesiologist, Anesthetistnurse, reason, Deliveryman_name):

        self.num_case_year = num_case_year ## int
        self.date = time.strftime('%d/%m/%Y') ## format current date as string
        self.num_case_month = num_case_month ##int
        self.room = room ## Admin access this variable
        self.building = building ## string
        self.evaluation = evaluation ## string
        self.Pre_evaluateNurse = Pre_evaluateNurse ## list string 1-2 nurse

        self.AN = AN ## patient's ID
        self.patientName = patientName ## string
        self.age = [age_hour, age_day, age_month, age_year] ## list = ['hours', 'day', 'month', 'year'] as string
        self.arrivePlace = arrivePlace ## string
        self.departPlace = departPlace ## string
        self.typeofOperation = typeofOperation ## string
        self.department = department ## string
        self.service = service ##string
        self.ASA = ASA ## string
        self.agent = ['Dormicum', 'Ephedrine', 'Ketamine'] ## list of agent
        self.agent_dose = [Dormicum, Ephedrine, Ketamine] ## list dose of each agents
        self.Anesthesia_technique = Anesthesia_technique ## list
        self.Combined_technique = Combined_technique ## list
        self.airwayManagement = airwayManagement ## string
        self.Anesthesia_time = [Anesthesia_start_time, Anesthesia_finish_time, Anesthesia_time, Anesthesiologist] ## ['Anesthesia start time', 'Anesthesia finish time', 'Anesthesia time', 'Anesthesiologist']
        self.Anesthetistnurse = Anesthetistnurse ## list 1-5 nurse
        self.reason = reason ## string The reason that the patient cannot suit for operation
        self.Deliveryman = Deliveryman_name ## string name

        def setnum_case_year(self, new_num_case_year, new_num_case_month, new_room):
            self.num_case_year = new_num_case_year
            self.num_case_month = new_num_case_month
            self.room = new_room

        def getnum_case_year(self):
            return [self.num_case_year, self.num_case_month, self.room]

        def setPlace(self, new_building, new_evaluation, new_arrivePlace, new_departPlace):
            self.building = new_building
            self.evaluation = new_evaluation  ## string
            self.arrivePlace = new_arrivePlace  ## string
            self.departPlace = new_departPlace  ## string

        def getPlace(self):
            return [self.building, self.evaluation, self.arrivePlace, self.departPlace]

        def setPre_evaluateNurse(self, new_Pre_evaluateNurse):
            self.Pre_evaluateNurse = new_Pre_evaluateNurse

        def getPre_evaluateNurse(self):
            return self.Pre_evaluateNurse

        def setPatientInfo(self, new_AN, new_patientName, new_age):
            self.AN = AN  ## patient's ID
            self.patientName = new_patientName  ## string
            self.age = new_age  ## list = ['hours', 'day', 'month', 'year'] as string

        def getPatientInfo(self):
            return [self.AN, self.patientName, self.age]

        def settypeofOperation(self, new_typeofOperation):
            self.typeofOperation = new_typeofOperation  ## string

        def gettypeofOperation(self):
            return self.typeofOperation

        def setdepartment(self, new_department):
            self.department = new_department  ## string

        def getdepartment(self):
            return department

        def setservice(self, new_service):
            self.service = new_service  ##string

        def getservice(self):
            return self.service

        def setASA(self, new_ASA):
            self.ASA = new_ASA  ## string

        def getASA(self):
            return self.ASA

        def setagent_dose(self, new_agent_dose):
            self.agent_dose = new_agent_dose  ## list dose of each agents

        def getagent_dose(self):
            return self.agent_dose

        def setAnesthesia_technique(self, new_Anesthesia_technique):
            self.Anesthesia_technique = new_Anesthesia_technique  ## list

        def getAnesthesia_technique(self):
            return self.Anesthesia_technique

        def setCombined_technique(self, new_Combined_technique):
            self.Combined_technique = new_Combined_technique  ## list

        def getCombined_technique(self):
            return self.Combined_technique

        def setairwayManagement(self, new_airwayManagement):
            self.airwayManagement = new_airwayManagement  ## string

        def getairwayManagement(self):
            return self.airwayManagement

        def setAnesthesia_time(self, new_Anesthesia_time):
            self.Anesthesia_time = new_Anesthesia_time

        def getAnesthesia_time(self):
            return self.Anesthesia_time

        def setAnesthetistnurse(self, new_Anesthetistnurse):
            self.Anesthetistnurse = new_Anesthetistnurse  ## list 1-5 nurse

        def getAnesthetistnurse(self):
            return self.Anesthetistnurse

        def setreason(self, new_reason):
            self.reason = new_reason  ## string The reason that the patient cannot suit for operation

        def getreason(self):
            return self.reason

        def setDeliveryman(self, new_Deliveryman):
            self.Deliveryman = Deliveryman_name  ## string name

        def getDeliveryman(self):
            return self.Deliveryman







