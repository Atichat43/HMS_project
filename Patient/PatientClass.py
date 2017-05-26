class Patient:
    def __init__(self, prepre_report):
        # "Type", "Date", "Time"
        # "Pre_OD", "Plan", "Underlying", "Treatment", "Note"
        self.OPD = ""
        self.AN = 0
        self.Pic = ""
        self.Name = ""
        self.Age = 0
        self.Phone = ""
        self.case_id = ""
        self.ExtraNote = []
        self.setBasicInfo(prepre_report[0])
        self.setExtraInfo(prepre_report[1])
        self.preReportDoctor = object
        self.preReportNurse = object
        self.intraReport = object
        self.postReport = []

    def getData(self):
        text = []
        text.append(self.AN)
        text.append(self.Name)
        text.append(self.Age)
        text.append(self.Phone)
        return text

    def setBasicInfo(self, part_basic_info):
        # ["OPD", "AN", "Pic", "Name", "Age", "Phone"]
        self.OPD = part_basic_info[0]
        self.AN = part_basic_info[1]
        self.Pic = part_basic_info[2]
        self.Name = part_basic_info[3]
        self.Age = part_basic_info[4]
        self.Phone = part_basic_info[5]
        self.case_id = part_basic_info[6]

    def setExtraInfo(self, part_extra_info):
        self.ExtraNote = part_extra_info

    def addPreReportDoctor(self, report):
        self.preReportDoctor = report

    def addPreReportNurse(self, report):
        self.preReportNurse = report

    def addIntraReport(self, report):
        self.intraReport = report

    def addPostReport(self, report):
        self.postReport.append(report)
