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
        pkl_file = open(self.file_name, 'rb')
        while True:
            try:
                obj = pickle.load(pkl_file)
            except EOFError:
                break
            object_list.append(obj)
        pkl_file.close()
        return object_list

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
    db = ControllerDatabase('userObject.pkl')
    s1 = Admin('A001', 'tiger', '4141', 'tiger', 'TG', '123456798')
    s2 = Admin('A002', 'boss', '1234', 'boss', 'AL', '123456798')
    s3 = Admin('A003', 'gift', '1234', 'gift', 'NU', '123456798')
    s4 = Doctor('D001', 'doc1', '1234', 'Dr.A', 'Charnchyyy', '00000', 'Sri tanya')
    s5 = Doctor('D002', 'doc2', '1234', 'Dr.B', 'MekboltZ', '00000', 'Sri tanya')
    s6 = Doctor('D003', 'doc3', '1234', 'Dr.C', 'Shadder4k', '00000', 'Overwatch')
    s7 = Nurse('N001', 'nur1', '1234', 'Nr.1', 'Aasdasdsad', '00000')
    s8 = Nurse('N002', 'nur2', '1234', 'Nr.1', 'rsmund', '58090043')
    s9 = Nurse('N003', 'nur3', '1234', 'Nr.1', 'Aatbat', '4114')
    s10 = RoomManager('R001', 'room1', '1234', 'Rr.1', 'Rommo', '65405')
    s11 = RoomManager('R002', 'room2', '1234', 'Rr.1', 'Roommmmm', '08999155314')
    s12 = RoomManager('R003', 'room3', '1234', 'Rr.1', 'ALALAAL', '68543120')
    s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
    db.updateObject(s)
    t = []
    lst = db.loadObj()
    for i in lst:
        print(i.getType())
        t.append(i)
    print(t)

