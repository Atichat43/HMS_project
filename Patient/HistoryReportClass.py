class HistoryReport(object):
    def __init__(self, patient_AN):
        self.patient_AN = patient_AN
        self.all_report = [] #[[pre_pre, pre, intra, post],[]]

    def addNewReport(self, new_report):
        if new_report is not None:
            self.all_report.append(new_report)

