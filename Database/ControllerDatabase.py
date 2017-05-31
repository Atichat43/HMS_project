from PySide.QtGui import QApplication

from Employee.Admin.AdminClass import *
from Employee.Doctor.DoctorClass import *
from Employee.Nurse.NurseClass import *
from Employee.Roommanager.RoommanagerClass import *
from Patient.ReportClass import PreReportPatientClass
from Patient.ReportClass import IntraReportPatientClass
from Patient.ReportClass import PostReportPatientClass
from Appointment import AppointmentClass
from Patient import HistoryReportClass

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


def demo_3REPORT():
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

    preReport1 = PreReportPatientClass.PreReportByNurse('atenolol 5 mg tab O at 6.00', '-', '-', '-', '-', 'Yes', '001',
                                                        'In', 'I', '2', '5',
                                                        '130/80', '86', '20', '36', 'E', 'Yes', 'Yes', 'Yes',
                                                        ['Med1', 'sym1', 'Med2', 'sym2', 'Med3', 'sym3'])

    preReport2 = PreReportPatientClass.PreReportByNurse('atenolol 5 mg tab O at 6.00', '-', '-', '-', '-', 'Yes', '001',
                                                        'In', 'I', '2', '5',
                                                        '130/80', '86', '20', '36', 'E', 'Yes', 'Yes', 'No',
                                                        ['-', '-', '-', '-', '-', '-'])

    intraReport = IntraReportPatientClass.IntraReportPatient('1234', '01/06/2017', '0001', '101', 'A', 'ICUS', 'ICUS',
                                                             ['Janet van Dyne', 'Wanda Maximoff'],
                                                             'post diagnose', 'operation', 'Major', 'Anes',
                                                             'Clinton Francis Barton', 'note',
                                                             'Pre anesthesia visit at ward', 'Official', 'I', '1', '1',
                                                             '1', '-', '-', 'Oral  Endotrachel Tracheal',
                                                             '8:30', '9:00', '30', '-',
                                                             ['Janet van Dyne', 'Wanda Maximoff',
                                                              'Natasha Alianovna Romanoff', 'Carol Danvers',
                                                              'Jennifer Walters'])

    intraReport2 = IntraReportPatientClass.IntraReportPatient('1111', '02/06/2017', '0002', '102', 'A', 'ICUS', 'ICUS',
                                                              ['Janet van Dyne', 'Wanda Maximoff'],
                                                              'post diagnose', 'operation', 'Major', 'Anes',
                                                              'Clinton Francis Barton', 'note',
                                                              'Pre anesthesia visit at ward', 'Official', 'I', '1', '1',
                                                              '1', '-', '-', 'Oral  Endotrachel Tracheal',
                                                              '8:30', '9:00', '30', '-',
                                                              ['Janet van Dyne', 'Wanda Maximoff',
                                                               'Natasha Alianovna Romanoff', 'Carol Danvers',
                                                               'Jennifer Walters'])

    post_report1 = ['Anes. Personal hazard', 'Awareness', 'Cardiac arrest', 'Note', 'Jacques Duquesne', 'Procedure',
                    '6/5/2017']
    post_report2 = ['CVA', 'Awareness', 'Diffcult intubation', 'Note', 'Jacques Duquesne', 'Procedure', '7/5/2017']

    post_report = PostReportPatientClass.PostReportPatient()
    post_report.setAnesthetic_complications_operationroom(post_report1)
    post_report.setAnesthetic_complications_admitroom(post_report1)
    post_report.setAnesthetic_complications_admitroom_2hrs(post_report1)
    post_report.setAnesthetic_complications_admitroom_24hrs(post_report2)
    post_report.setAnesthetic_complications_procedure(post_report2)
    post_report.setAnesthetic_complications_admitroom_48hrs(post_report2)
    post_report.setAnesthetic_complications_admitroom_7day(post_report2)

    p1.addPreReportNurse(preReport1)
    p1.addIntraReport(intraReport)
    p1.addPostReport(post_report)
    print(type(preReport1))
    print(type(intraReport))
    print(type(post_report))

    import sys
    app = QApplication(sys.argv)
    # from Employee.Doctor.GuiClass import Dialog_3ReportPatientClass as R
    # win = R.ReportPatient()
    # pre_data, pre_databox = p1.getPreInfo()
    # intra_data, intra_databox = p1.getIntraInfo()
    # post_data = p1.getPostInfo()
    # win.setDataFromDataBasePre(pre_data, pre_databox)
    # win.setDataFromDataBaseIntra(intra_data, intra_databox)
    # win.setDataFromDataBasePost(post_data)
    """THIS HERE"""
    from Patient import Widget_HistoryReport as h
    win = h.HistoryReport(preReport1, intraReport, post_report)
    win.show()
    win.exec_()
    sys.exit(app.exec_())


def demo_admin():
    con = ControllerDatabase('userObject.pkl')
    lst = con.loadObj()
    lst = []

    a1 = Admin('A001', 'tiger', '1234', 'Sirapop', 'Issariyodom', '0971591691')
    a2 = Admin('A002', 'boss', '1234', 'Atichat', 'Lappanopakorn', '123465789')
    lst.append(a1)
    lst.append(a2)

    con.updateObject(lst)


def demo_nurse():
    con = ControllerDatabase('userObject.pkl')
    lst = con.loadObj()

    n1 = Nurse('N001', 'Nur1', '1234', 'N.A', 'ASDFG', '0245678123')
    n2 = Nurse('N002', 'Nur2', '1234', 'N.B', 'Lappanopakorn', '123465789')
    lst.append(n1)
    lst.append(n2)

    con.updateObject(lst)


def demo_doctor():
    con = ControllerDatabase('userObject.pkl')
    lst = con.loadObj()

    a1 = Doctor('D001', 'Doc1', '1234', 'Doc.A', 'drrrrrA', '0971591691', 'A')
    a2 = Doctor('D002', 'Doc2', '1234', 'Doc.B', 'DrrrrrB', '123465789', 'B')
    lst.append(a1)
    lst.append(a2)

    con.updateObject(lst)


def demo_patient():
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

    """update status"""
    p1.updateStatus(s.PatientStatus.waitingPreReport)
    p2.updateStatus(s.PatientStatus.waitingPreReport)
    p3.updateStatus(s.PatientStatus.waitingPreReport)

    db_patients.updateObject([p1, p2, p3])
    doctor = Doctor('D001', 'doc1', '1234', 'Dr.A', 'Charnchyyy', '00000', 'Sri tanya')
    s1 = AppointmentClass.Appointment('10001', ["Elective case", "28/5/2017", "Morning"], doctor, p1)
    s2 = AppointmentClass.Appointment('10002', ["Emergency case", "28/5/2017", "Afternoon"], doctor, p2)
    s3 = AppointmentClass.Appointment('10003', ["Ergency case", "28/5/2017", "None"], doctor, p3)
    print(s3.patient.AN)
    print(p3.AN)
    db_appointment.updateObject([s1, s2, s3])

    preReport1 = PreReportPatientClass.PreReportByNurse('atenolol 5 mg tab O at 6.00', '-', '-', '-', '-', 'Yes', '001',
                                                        'In', 'I', '2', '5',
                                                        '130/80', '86', '20', '36', 'E', 'Yes', 'Yes', 'Yes',
                                                        ['Med1', 'sym1', 'Med2', 'sym2', 'Med3', 'sym3'])

    preReport2 = PreReportPatientClass.PreReportByNurse('atenolol 5 mg tab O at 6.00', '-', '-', '-', '-', 'Yes', '001',
                                                        'In', 'I', '2', '5',
                                                        '130/80', '86', '20', '36', 'E', 'Yes', 'Yes', 'No',
                                                        ['-', '-', '-', '-', '-', '-'])

    intraReport = IntraReportPatientClass.IntraReportPatient('1234', '01/06/2017', '0001', '101', 'A', 'ICUS', 'ICUS',
                                                             ['Janet van Dyne', 'Wanda Maximoff'],
                                                             'post diagnose', 'operation', 'Major', 'Anes',
                                                             'Clinton Francis Barton', 'note',
                                                             'Pre anesthesia visit at ward', 'Official', 'I', '1', '1',
                                                             '1', '-', '-', 'Oral  Endotrachel Tracheal',
                                                             '8:30', '9:00', '30', '-',
                                                             ['Janet van Dyne', 'Wanda Maximoff',
                                                              'Natasha Alianovna Romanoff', 'Carol Danvers',
                                                              'Jennifer Walters'])

    intraReport2 = IntraReportPatientClass.IntraReportPatient('1111', '02/06/2017', '0002', '102', 'A', 'ICUS', 'ICUS',
                                                              ['Janet van Dyne', 'Wanda Maximoff'],
                                                              'post diagnose', 'operation', 'Major', 'Anes',
                                                              'Clinton Francis Barton', 'note',
                                                              'Pre anesthesia visit at ward', 'Official', 'I', '1', '1',
                                                              '1', '-', '-', 'Oral  Endotrachel Tracheal',
                                                              '8:30', '9:00', '30', '-',
                                                              ['Janet van Dyne', 'Wanda Maximoff',
                                                               'Natasha Alianovna Romanoff', 'Carol Danvers',
                                                               'Jennifer Walters'])

    post_report1 = ['Anes. Personal hazard', 'Awareness', 'Cardiac arrest', 'Note', 'Jacques Duquesne', 'Procedure',
                    '6/5/2017']
    post_report2 = ['CVA', 'Awareness', 'Diffcult intubation', 'Note', 'Jacques Duquesne', 'Procedure', '7/5/2017']

    post_report = PostReportPatientClass.PostReportPatient()
    post_report.setAnesthetic_complications_operationroom(post_report1)
    post_report.setAnesthetic_complications_admitroom(post_report1)
    post_report.setAnesthetic_complications_admitroom_2hrs(post_report1)
    post_report.setAnesthetic_complications_admitroom_24hrs(post_report2)
    post_report.setAnesthetic_complications_procedure(post_report2)
    post_report.setAnesthetic_complications_admitroom_48hrs(post_report2)
    post_report.setAnesthetic_complications_admitroom_7day(post_report2)

    """update status"""
    p2.addPreReportNurse(preReport1)
    p2.updateStatus(s.PatientStatus.waitingIntraReport)
    p3.addPreReportNurse(preReport2)
    p3.updateStatus(s.PatientStatus.waitingIntraReport)

    p3.addIntraReport(intraReport)
    p3.updateStatus(s.PatientStatus.waitingPostReport)

    p3.addPostReport(post_report)
    p3.updateStatus(s.PatientStatus.done)
    db_patients.updateObject([p1, p2, p3])


def demo_appointment():
    con = ControllerDatabase('userObject.pkl')
    lst = con.loadObj()

    for i in lst:
        if i.username == 'Doc1':
            doc1 = i

    con1 = ControllerDatabase('patientObject.pkl')
    lst1 = con1.loadObj()

    for j in lst1:
        if j.AN == '0001':
            pat1 = j

    a = AppointmentClass.Appointment('10001', ['Elective case', '1/6/2017', 'None'], doc1, pat1)
    a1 = AppointmentClass.Appointment('10002', ['Emergency case', '31/5/2017', 'Morning'], doc1, pat1)
    a2 = AppointmentClass.Appointment('10003', ['Elective case', '31/5/2017', 'Afternoon'], doc1, pat1)
    a3 = AppointmentClass.Appointment('10004', ['Elective case', '20/5/2017', 'None'], doc1, pat1)
    a4 = AppointmentClass.Appointment('10005', ['Elective case', '20/5/2017', 'Afternoon'], doc1, pat1)

    appointments = [a, a1, a2, a3, a4]
    con2 = ControllerDatabase('appointmentObject.pkl')
    lst2 = con2.loadObj()

    lst2 += appointments

    con2.updateObject(lst2)


def demo_History():
    c = ControllerDatabase("reportObject.pkl")
    lst = c.loadObj()
    lst = []
    n = ControllerDatabase("patientObject.pkl")
    n_lst = n.loadObj()
    for patient in n_lst:
        print(patient.AN)
        l = HistoryReportClass.HistoryReport(patient.AN, patient.preReportDoctor, patient.preReportNurse,
                                             patient.intraReport, patient.postReport)
        l.addNewReport([patient.preReportDoctor, patient.preReportNurse, patient.intraReport, patient.postReport])

        l1 = HistoryReportClass.HistoryReport(patient.AN)
        l1.addNewReport([patient.preReportDoctor, patient.preReportNurse, patient.intraReport, patient.postReport])

        lst.append(l)
        lst.append(l1)
    print(lst)
    print(len(lst))
    c.updateObject(lst)


def main():
    demo_admin()
    demo_nurse()
    demo_doctor()
    demo_patient()
    demo_appointment()
    # demo_History()

##main()
