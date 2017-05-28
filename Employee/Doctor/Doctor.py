from Database import ControllerDatabase
import Setting as s


class DoctorApplication(object):
    def __init__(self):
        self.current_case_id = ""
        self.ctrlDatabase_patient = ControllerDatabase.ControllerDatabase(s.DB_PATIENT)
        self.ctrlDatabase_appointment = ControllerDatabase.ControllerDatabase(s.DB_APPOINTMENT)

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
        patients.append(newPatient)
        self.ctrlDatabase_patient.updateObject(patients)
        #update case_id

    def editPatient(self, newPatient):
        patients = self.getPatientFromDatabase()
        for i in range(len(patients)):
            #edit check by case_id instead
            if patients[i].AN == newPatient.AN:
                patients[i] = newPatient
                break
        self.ctrlDatabase_patient.updateObject(patients)

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
        print("called getAppByDoctor")
        print(len(appointments))
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


if __name__ == "__main__":
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    win = DoctorApplication()
    print(win.getCurrentCaseID())
    print()
    exit(app.exec_())
