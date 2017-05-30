from Database import ControllerDatabase
import Setting as s


class NurseApplication(object):
    def __init__(self):
        self.current_case_id = ""
        self.ctrlDatabase_patient = ControllerDatabase.ControllerDatabase(s.DB_PATIENT)
        self.ctrlDatabase_appointment = ControllerDatabase.ControllerDatabase(s.DB_APPOINTMENT)

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

    def getAppointmentByAN(self, AN):
        appointments = self.getAppointmentFromDatabase()
        for appointment in appointments:
            if appointment.patient.AN == AN:
                return appointment
        return None

    def getAppointmentFromDatabase(self):
        obj_appointments = self.ctrlDatabase_appointment.loadObj()
        return obj_appointments
