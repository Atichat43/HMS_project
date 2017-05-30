from Database import ControllerDatabase
import Setting as s


class NurseApplication(object):
    def __init__(self):
        self.current_case_id = ""
        self.ctrlDatabase_patient = ControllerDatabase.ControllerDatabase(s.DB_PATIENT)
        self.ctrlDatabase_appointment = ControllerDatabase.ControllerDatabase(s.DB_APPOINTMENT)
        self.ctrlDatabase_history = ControllerDatabase.ControllerDatabase(s.DB_REPORT)

    """PATIENT DATABASE"""
    def getPatientFromDatabase(self):
        obj_patients = self.ctrlDatabase_patient.loadObj()
        return obj_patients

    def editPatient(self, newPatient):
        patients = self.getPatientFromDatabase()
        for i in range(len(patients)):
            if patients[i].AN == newPatient.AN:
                patients[i] = newPatient
                break
        self.ctrlDatabase_patient.updateObject(patients)

    def getPatientByAN(self, AN):
        patients = self.getPatientFromDatabase()
        for patient in patients:
            if patient.AN == AN:
                return patient
        return None

    """APPOINTMENT DATABASE"""
    def getAppointmentFromDatabase(self):
        obj_appointments = self.ctrlDatabase_appointment.loadObj()
        return obj_appointments

    def getAppointmentByAN(self, AN):
        appointments = self.getAppointmentFromDatabase()
        for appointment in appointments:
            if appointment.patient.AN == AN:
                return appointment
        return None

    """REPORT DATABASE"""
    def getReportFromDatabase(self):
        obj_reports = self.ctrlDatabase_report.loadObj()
        return obj_reports

    def getReportByAN(self, AN):
        reports = self.getReportFromDatabase()
        for report in reports:
            if report.patient_AN == AN:
                return report
        return None

    """------------------------History Database---------------------"""

    def getHistoryReport(self):
        return self.ctrlDatabase_history.loadObj()

    def getHistoryReportByAN(self, AN):
        history_reports = self.getHistoryReport()
        print("GET -HISROTY REPORTS AN")
        print(history_reports)
        for report in history_reports:
            if report.patient_AN == AN:
                return report.all_report
        return None

    def createHistory(self, new_history_report):
        hr = self.getHistoryReport()
        hr.append(new_history_report)
        self.ctrlDatabase_history.updateObject(hr)