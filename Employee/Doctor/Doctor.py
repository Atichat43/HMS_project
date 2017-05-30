from Database import ControllerDatabase
import Setting as s


class DoctorApplication(object):
    def __init__(self):
        self.current_case_id = ""
        self.ctrlDatabase_patient = ControllerDatabase.ControllerDatabase(s.DB_PATIENT)
        self.ctrlDatabase_appointment = ControllerDatabase.ControllerDatabase(s.DB_APPOINTMENT)
        self.ctrlDatabase_history = ControllerDatabase.ControllerDatabase(s.DB_REPORT)

    def getCurrentCaseID(self):
        patients = self.getPatientFromDatabase()
        last_patients_id = patients[-1].case_id
        self.current_case_id = last_patients_id
        return self.current_case_id

    """-------------------------Patient Database---------------------------------------------"""
    def getPatientFromDatabase(self):
        obj_patients = self.ctrlDatabase_patient.loadObj()
        #update case id
        return obj_patients

    def addNewPatient(self, newPatient):
        patients = self.getPatientFromDatabase()
        newPatient.updateStatus(s.PatientStatus.waitingPreReport)
        patients.append(newPatient)
        self.ctrlDatabase_patient.updateObject(patients)
        #update case_id

    def editPatient(self, newPatient):
        patients = self.getPatientFromDatabase()
        for i in range(len(patients)):
            if patients[i].AN == newPatient.AN:
                patients[i] = newPatient
                break
        self.ctrlDatabase_patient.updateObject(patients)

    def patientValid(self, AN): #iSAvailableAN: True if not exist False is exist
        patients = self.getPatientFromDatabase()
        for patient in patients:
            if patient.AN == AN:
                return False #exist
        return True

    def oldPatientValid(self, AN, patient_name):
        patients = self.getPatientFromDatabase()
        for patient in patients:
            if patient.AN == AN:
                if patient.Name == patient_name:
                    return True
        return False

    """-------------------------Appointment Database---------------------------------------------"""
    def getAppointmentFromDatabase(self):
        obj_appointments = self.ctrlDatabase_appointment.loadObj()
        return obj_appointments

    def getAppointmentByDoctor(self, doctor_id):
        all_appointments = self.getAppointmentFromDatabase()
        appointments = []
        for appointment in all_appointments:
            if appointment.doctor.id == doctor_id:
                appointments.append(appointment)
        return appointments

    def addNewAppointment(self, newAppointment):
        appointments = self.getAppointmentFromDatabase()
        appointments.append(newAppointment)
        self.ctrlDatabase_appointment.updateObject(appointments)
        #update case_id

    def editAppointment(self, newAppointment):
        appointments = self.getAppointmentFromDatabase()
        for i in range(len(appointments)):
            if appointments[i].AN == newAppointment.case_id:
                appointments[i] = newAppointment
                break
        self.ctrlDatabase_patient.updateObject(appointments)

    def appointmentValid(self, date, time, doctor):
        appointments = self.getAppointmentByDoctor(doctor.id)
        for am in appointments:
            if am.date.getDate() == date and am.time == time and am.doctor.firstname == doctor.firstname:
                print("Already exist Appointment at this time")
                print("   Date:" + am.date.getDate() + " " + str(date))
                print("   Time:" + str(am.time) + " " + str(time))
                print("   Doctor:" + str(am.doctor.firstname) + " " + str(doctor.firstname))
                print()
                return False
        return True

    def getPatientByCaseId(self, case_id, doctor_id):
        appointments = self.getAppointmentByDoctor(doctor_id)
        for am in appointments:
            if am.case_id == case_id:
                return am.patient
        return None

    def getAppointmentByAN(self, AN):
        appointments = self.getAppointmentFromDatabase()
        for appointment in appointments:
            if appointment.patient.AN == AN:
                return appointment
        return None

    """-------------------------History Database---------------------------------------------"""
    def getHistoryReport(self):
        return self.ctrlDatabase_history.loadObj()

    def getHistoryReportByAN(self, AN):
        history_reports = self.getHistoryReport()
        for report in history_reports:
            if report.patient_AN == AN:
                return report
        return None
