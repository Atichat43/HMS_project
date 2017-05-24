from Employee.Admin import AdminClass
from Employee.Doctor import DoctorClass
from Employee.Nurse import NurseClass
from Employee.Roommanager import RoommanagerClass
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


class ContorllerDatabase(object):
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

