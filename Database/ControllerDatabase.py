from Employee.Admin.AdminClass import *
from Employee.Doctor.DoctorClass import *
from Employee.Nurse.NurseClass import *
from Employee.Roommanager.RoommanagerClass import *
'''
import pickle, pprint

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()



pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
##pprint.pprint(data1)
print(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
'''
import pickle


class ControllerDatabase(object):
    def __init__(self, filename):
        self.file_name = filename

    def loadObj(self):
        object_list = []
        try:
            pkl_file = open(self.file_name, 'rb')
            while True:
                try:
                    obj = pickle.load(pkl_file)
                except EOFError:
                    break
                object_list.append(obj)
            pkl_file.close()
            return object_list
        except IOError:
            print("New PKL file created: " + str(self.file_name))
            self.newObject(object)
            print("created success")

    def updateObject(self, lst):
        pkl_file = open(self.file_name, 'wb')
        for i in range(len(lst)):
            pickle.dump(lst[i], pkl_file)
        pkl_file.close()

    def newObject(self, ob):
        pkl_file = open(self.file_name, 'wb')
        pickle.dump(ob, pkl_file)
        pkl_file.close()



def demo():
    from Appointment import AppointmentClass
    from Patient import PatientClass
    db_appointment = ControllerDatabase('appointmentObject.pkl')
    db_patients = ControllerDatabase('patientObject.pkl')
    pre_pre_report = [["OPD", "0001", "PIC", "Atichat Lappanopakon", 20, "0971249197", "10001"],
                      ["Pre_OD", "Plan", "Underlying", "Treatment", "Note"]]
    p1 = PatientClass.Patient(pre_pre_report)
    pre_pre_report = [["IPD", "0002", "PIC", "David Jason", 10, "0871249197", "10002"],
                      ["Pre_OD", "Plan", "Underlying", "Treatment", "Note"]]
    p2 = PatientClass.Patient(pre_pre_report)
    pre_pre_report = [["OPD", "0003", "PIC", "Sara MJ", 40, "0271249197", "10003"],
                      ["Pre_OD", "Plan", "Underlying", "Treatment", "Note"]]
    p3 = PatientClass.Patient(pre_pre_report)
    db_patients.updateObject([p1, p2, p3])
    doctor = Doctor('D001', 'doc1', '1234', 'Dr.A', 'Charnchyyy', '00000', 'Sri tanya')
    s1 = AppointmentClass.Appointment('10001', ["Elective case", "28/5/2017", "Morning"], doctor, p1)
    s2 = AppointmentClass.Appointment('10002', ["Emergency case", "28/5/2017", "Afternoon"], doctor, p2)
    s3 = AppointmentClass.Appointment('10003', ["Ergency case", "28/5/2017", "None"], doctor, p3)
    db_appointment.updateObject([s1, s2, s3])



