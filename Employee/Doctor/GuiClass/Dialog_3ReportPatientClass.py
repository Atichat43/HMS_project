from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader

from Base.Dialog_MsgBox import ConfirmMsgClass
from Patient.ReportClass import PreReportPatientClass
from Patient.ReportClass import IntraReportPatientClass
from Patient.ReportClass import PostReportPatientClass

import Setting as s


class ReportPatient(QDialog):
    def __init__(self, parent = None):
        super(ReportPatient, self).__init__(parent)
        posX, posY, sizeW, sizeH = s.GEOMETRY_DIALOG_3REPORT
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.loader = QUiLoader()
        self.ui = self.loader.load(s.PATH_DOCTOR_DIALOG_3REPORT, self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.ui)
        self.initContainer()
        self.initPostButtons(self.ui)
        self.initIntraButtons(self.ui)
        self.initPreButtons(self.ui)
        self.forDev()

    def initContainer(self):
        self.pre_info_line = []
        self.pre_info_box = []
        self.intra_info_line = []
        self.intra_info_box = []
        self.post1_info = []
        self.post2_info = []
        self.post3_info = []
        self.post4_info = []
        self.post5_info = []
        self.post6_info = []
        self.post7_info = []

    """PRE REPORT"""
    def initPreButtons(self,ui):
        #Line edits
        self.lineEditPrelist = []
        for i in range(1, 20, 1):
            name = "PreLineEdit_" + str(i)
            line = ui.findChild(QLineEdit, name)
            self.lineEditPrelist.append(line)

        #Combo box
        self.comboBoxPrelist = []
        for i in range(1, 8, 1):
            name = "PrecomboBox_" + str(i)
            box = ui.findChild(QComboBox, name)
            self.comboBoxPrelist.append(box)
        self.b_pre_save = ui.findChild(QPushButton, "save_pre_Button")
        self.b_pre_cancel = ui.findChild(QPushButton, "cancel_pre_Button")
        self.b_pre_save.clicked.connect(self.save_pre_info)
        self.b_pre_cancel.clicked.connect(self.cancel)

    def getPreData(self,ui):
        for item in self.lineEditPrelist:
            self.pre_info_line.append(item.text())

        for box in self.comboBoxPrelist:
            self.pre_info_box.append(box.currentText())

    def save_pre_info(self):
        self.getPreData(self.ui)
        #[premed, PRC, FFP, Plt, PC, plannedICU, fullBed, service, ASA, BW, HT, BP, P, RR, T, GCS1, GCS2, smoking, alcoholic, allergy]
        lt = [(self.pre_info_line[13],self.pre_info_line[14]),(self.pre_info_line[15],self.pre_info_line[16]),(self.pre_info_line[17],self.pre_info_line[18])]
        preReport = PreReportPatientClass.PreReportByNurse(self.pre_info_line[0],self.pre_info_line[1],self.pre_info_line[2],self.pre_info_line[3],self.pre_info_line[4],self.pre_info_box[0],self.pre_info_line[5],
                                                           self.pre_info_box[1],self.pre_info_box[2],self.pre_info_line[6],self.pre_info_line[7],self.pre_info_line[8],self.pre_info_line[9],self.pre_info_line[10],
                                                           self.pre_info_line[11],self.pre_info_line[12],self.pre_info_box[3],self.pre_info_box[4],self.pre_info_box[5],self.pre_info_box[6])

        self.close()

    """INTRA REPORT"""
    def initIntraButtons(self, ui):
        #Line edit
        self.lineEditIntralist = []
        for i in range(1, 22, 1):
            name = "IntraEditLine_" + str(i)
            line = ui.findChild(QLineEdit, name)
            self.lineEditIntralist.append(line)

        #Combo box
        self.comboBoxIntralist = []
        for i in range(1, 13, 1):
            name = "IntracomboBox_" + str(i)
            box = ui.findChild(QComboBox, name)
            self.comboBoxIntralist.append(box)

        self.b_intra_save = ui.findChild(QPushButton, "save_intra_Button")
        self.b_intra_cancel = ui.findChild(QPushButton, "cancel_intra_Button")
        self.b_intra_save.clicked.connect(self.save_intra_info)
        self.b_intra_cancel.clicked.connect(self.cancel)

    def getIntraData(self):
        for item in self.lineEditIntralist:
            self.intra_info_line.append(item.text())

        for box in self.comboBoxIntralist:
            self.intra_info_box.append(box.currentText())

    def save_intra_info (self):
        self.getIntraData()
        intraReport = IntraReportPatientClass.IntraReportPatient(self.intra_info_line[0], self.intra_info_line[1], self.intra_info_line[2], self.intra_info_line[3], self.intra_info_box[0], self.intra_info_box[1], self.intra_info_box[2], self.intra_info_line[4], [self.intra_info_line[5], self.intra_info_line[6]], self.intra_info_line[7], self.intra_info_box[3], self.intra_info_box[4],
                                        self.intra_info_line[8], self.intra_info_line[9], self.intra_info_box[5], self.intra_info_box[6], self.intra_info_box[7], self.intra_info_line[10], self.intra_info_line[11], self.intra_info_line[12], self.intra_info_box[8], self.intra_info_box[9], self.intra_info_box[10],
                                        self.intra_info_line[13], self.intra_info_line[14], self.intra_info_line[15], self.intra_info_box[11], [self.intra_info_line[16], self.intra_info_line[17], self.intra_info_line[18], self.intra_info_line[19],self.intra_info_line[20]])
        self.close()

    """POST REPORT"""
    def initPostButtons(self, ui):
        #post1
        self.post1List = []
        comboBoxPost1list = []
        for i in range(1, 4, 1):
            name = "post1_comboBox_" + str(1)
            box = ui.findChild(QComboBox, name)
            comboBoxPost1list.append(box)
        self.post1List.append(comboBoxPost1list)
        line1 = ui.findChild(QLineEdit, "post1_lineEdit_1")
        line2 = ui.findChild(QLineEdit, "post1_lineEdit_2")
        self.post1List.append(line1)
        self.post1List.append(line2)

        box = ui.findChild(QComboBox, "post1_comboBox")
        self.post1List.append(box)

        dmy = ui.findChild(QDateEdit, "post1_dateEdit")
        self.post1List.append(dmy)

        # post2
        self.post2List = []
        comboBoxPost2list = []
        for i in range(1, 4, 1):
            name = "post2_comboBox_" + str(1)
            box = ui.findChild(QComboBox, name)
            comboBoxPost2list.append(box)
        self.post2List.append(comboBoxPost2list)

        line1 = ui.findChild(QLineEdit, "post2_lineEdit_1")
        line2 = ui.findChild(QLineEdit, "post2_lineEdit_2")
        self.post2List.append(line1)
        self.post2List.append(line2)

        box = ui.findChild(QComboBox, "post2_comboBox")
        self.post2List.append(box)

        dmy = ui.findChild(QDateEdit, "post2_dateEdit")
        self.post2List.append(dmy)

        # post3
        self.post3List = []
        comboBoxPost3list = []
        for i in range(1, 4, 1):
            name = "post3_comboBox_" + str(1)
            box = ui.findChild(QComboBox, name)
            comboBoxPost3list.append(box)
        self.post3List.append(comboBoxPost3list)

        line1 = ui.findChild(QLineEdit, "post3_lineEdit_1")
        line2 = ui.findChild(QLineEdit, "post3_lineEdit_2")
        self.post3List.append(line1)
        self.post3List.append(line2)

        box = ui.findChild(QComboBox, "post3_comboBox")
        self.post3List.append(box)

        dmy = ui.findChild(QDateEdit, "post3_dateEdit")
        self.post3List.append(dmy)

        # post4
        self.post4List = []
        comboBoxPost4list = []
        for i in range(1, 4, 1):
            name = "post4_comboBox_" + str(1)
            box = ui.findChild(QComboBox, name)
            comboBoxPost4list.append(box)
        self.post4List.append(comboBoxPost4list)

        line1 = ui.findChild(QLineEdit, "post4_lineEdit_1")
        line2 = ui.findChild(QLineEdit, "post4_lineEdit_2")
        self.post4List.append(line1)
        self.post4List.append(line2)

        box = ui.findChild(QComboBox, "post4_comboBox")
        self.post4List.append(box)

        dmy = ui.findChild(QDateEdit, "post4_dateEdit")
        self.post4List.append(dmy)

        # post5
        self.post5List = []
        comboBoxPost5list = []
        for i in range(1, 4, 1):
            name = "post5_comboBox_" + str(1)
            box = ui.findChild(QComboBox, name)
            comboBoxPost5list.append(box)
        self.post5List.append(comboBoxPost5list)

        line1 = ui.findChild(QLineEdit, "post5_lineEdit_1")
        line2 = ui.findChild(QLineEdit, "post5_lineEdit_2")
        self.post5List.append(line1)
        self.post5List.append(line2)

        box = ui.findChild(QComboBox, "post5_comboBox")
        self.post5List.append(box)

        dmy = ui.findChild(QDateEdit, "post5_dateEdit")
        self.post5List.append(dmy)

        # post6
        self.post6List = []
        comboBoxPost6list = []
        for i in range(1, 4, 1):
            name = "post6_comboBox_" + str(1)
            box = ui.findChild(QComboBox, name)
            comboBoxPost6list.append(box)
        self.post6List.append(comboBoxPost6list)

        line1 = ui.findChild(QLineEdit, "post6_lineEdit_1")
        line2 = ui.findChild(QLineEdit, "post6_lineEdit_2")
        self.post6List.append(line1)
        self.post6List.append(line2)

        box = ui.findChild(QComboBox, "post6_comboBox")
        self.post6List.append(box)

        dmy = ui.findChild(QDateEdit, "post6_dateEdit")
        self.post6List.append(dmy)

        # post7
        self.post7List = []
        comboBoxPost7list = []
        for i in range(1, 4, 1):
            name = "post7_comboBox_" + str(1)
            box = ui.findChild(QComboBox, name)
            comboBoxPost7list.append(box)
        self.post7List.append(comboBoxPost7list)

        line1 = ui.findChild(QLineEdit, "post7_lineEdit_1")
        line2 = ui.findChild(QLineEdit, "post7_lineEdit_2")
        self.post7List.append(line1)
        self.post7List.append(line2)

        box = ui.findChild(QComboBox, "post7_comboBox")
        self.post7List.append(box)

        dmy = ui.findChild(QDateEdit, "post7_dateEdit")
        self.post7List.append(dmy)

        self.b_post_save = ui.findChild(QPushButton, "save_post_Button")
        self.b_post_cancel = ui.findChild(QPushButton, "cancel_post_Button")
        self.b_post_save.clicked.connect(self.save_post_info)
        self.b_post_cancel.clicked.connect(self.cancel)

    def getPostData(self,ui):
        #post1
        self.post1_info.append(self.post1List[0][0].currentText())
        self.post1_info.append(self.post1List[0][1].currentText())
        self.post1_info.append(self.post1List[0][2].currentText())
        self.post1_info.append(self.post1List[1].text())
        self.post1_info.append(self.post1List[2].text())
        self.post1_info.append(self.post1List[3].currentText())
        self.post1_info.append(self.post1List[4].currentSection())

        # post2
        self.post2_info.append(self.post2List[0][0].currentText())
        self.post2_info.append(self.post2List[0][1].currentText())
        self.post2_info.append(self.post2List[0][2].currentText())
        self.post2_info.append(self.post2List[1].text())
        self.post2_info.append(self.post2List[2].text())
        self.post2_info.append(self.post2List[3].currentText())
        self.post2_info.append(self.post2List[4].currentSection())

        # post3
        self.post3_info.append(self.post3List[0][0].currentText())
        self.post3_info.append(self.post3List[0][1].currentText())
        self.post3_info.append(self.post3List[0][2].currentText())
        self.post3_info.append(self.post3List[1].text())
        self.post3_info.append(self.post3List[2].text())
        self.post3_info.append(self.post3List[3].currentText())
        self.post3_info.append(self.post3List[4].currentSection())

        # post4
        self.post4_info.append(self.post4List[0][0].currentText())
        self.post4_info.append(self.post4List[0][1].currentText())
        self.post4_info.append(self.post4List[0][2].currentText())
        self.post4_info.append(self.post4List[1].text())
        self.post4_info.append(self.post4List[2].text())
        self.post4_info.append(self.post4List[3].currentText())
        self.post4_info.append(self.post4List[4].currentSection())

        # post5
        self.post5_info.append(self.post5List[0][0].currentText())
        self.post5_info.append(self.post5List[0][1].currentText())
        self.post5_info.append(self.post5List[0][2].currentText())
        self.post5_info.append(self.post5List[1].text())
        self.post5_info.append(self.post5List[2].text())
        self.post5_info.append(self.post5List[3].currentText())
        self.post5_info.append(self.post5List[4].currentSection())

        # post6
        self.post6_info.append(self.post6List[0][0].currentText())
        self.post6_info.append(self.post6List[0][1].currentText())
        self.post6_info.append(self.post6List[0][2].currentText())
        self.post6_info.append(self.post6List[1].text())
        self.post6_info.append(self.post6List[2].text())
        self.post6_info.append(self.post6List[3].currentText())
        self.post6_info.append(self.post6List[4].currentSection())

        # post7
        self.post7_info.append(self.post7List[0][0].currentText())
        self.post7_info.append(self.post7List[0][1].currentText())
        self.post7_info.append(self.post7List[0][2].currentText())
        self.post7_info.append(self.post7List[1].text())
        self.post7_info.append(self.post7List[2].text())
        self.post7_info.append(self.post7List[3].currentText())
        self.post7_info.append(self.post7List[4].currentSection())

    def save_post_info (self):
        self.getPostData(self.ui)
        post_report = PostReportPatientClass.PostReportPatient()
        post_report.setAnesthetic_complications_operationroom(self.post1_info)
        post_report.setAnesthetic_complications_admitroom(self.post2_info)
        post_report.setAnesthetic_complications_admitroom_2hrs(self.post3_info)
        post_report.setAnesthetic_complications_admitroom_24hrs(self.post4_info)
        post_report.setAnesthetic_complications_procedure(self.post5_info)
        post_report.setAnesthetic_complications_admitroom_48hrs(self.post6_info)
        post_report.setAnesthetic_complications_admitroom_7day(self.post7_info)
        self.close()

    def cancel(self):
        dialog = ConfirmMsgClass.ConfirmYesNo()
        if dialog.ans == True:
            print("Discard")
            self.close()
        else:
            print("Cancel")

    """ FOR DEVELOP"""
    def forDev(self):
        self.forDevPre()
        self.forDevIntra()
        self.forDevPost()

    def forDevPre(self):
        pre = ['atenolol 5 mg tab O at 6.00', '-', '-', '-', '-', '001', '2', '5', '20.11', '130/80', '86', '20',
               '36', 'Med1', 'sym1', 'Med2', 'sym2', 'Med3', 'sym3']
        count = 0
        print(len(self.lineEditPrelist),len(pre))
        for i in self.lineEditPrelist:
            s = pre[count]
            i.setText(s)
            count+=1
        print("done FORDEV")

    def forDevIntra(self):
        intra = ['1234', '01/06/2017', '0001', '101', 'Janet van Dyne', 'Wanda Maximoff',
                 'post diagnose', 'operation', 'Clinton Francis Barton', 'note', '1', '1', '1',
                 '8:30', '9:00', '30', 'Janet van Dyne', 'Wanda Maximoff', 'Natasha Alianovna Romanoff',
                 'Carol Danvers', 'Jennifer Walters']
        count = 0
        for i in self.lineEditIntralist:
            s = intra[count]
            i.setText(s)
            count+=1

    def forDevPost(self):
        post = ['Note', 'Monica Rambeau']
        self.post1List[1].setText(post[0])
        self.post1List[2].setText(post[1])

        self.post2List[1].setText(post[0])
        self.post2List[2].setText(post[1])

        self.post3List[1].setText(post[0])
        self.post3List[2].setText(post[1])

        self.post4List[1].setText(post[0])
        self.post4List[2].setText(post[1])

        self.post5List[1].setText(post[0])
        self.post5List[2].setText(post[1])

        self.post6List[1].setText(post[0])
        self.post6List[2].setText(post[1])

        self.post7List[1].setText(post[0])
        self.post7List[2].setText(post[1])






