import sys

from PySide.QtCore import QDateTime, Qt

from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
from Patient.view import *
import Setting as s


class ReportPatient(QDialog):
    def __init__(self, parent = None):
        super(ReportPatient, self).__init__(parent)
        posX, posY, sizeW, sizeH = s.GEOMETRY_DIALOG_3REPORT
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.loader = QUiLoader()
        ui = self.loader.load(s.PATH_DOCTOR_DIALOG_3REPORT, self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(ui)
        self.initPostButtons(ui)
        self.initIntraButtons(ui)
        self.initPreButtons(ui)


    def initPreButtons(self,ui):
        #Line edits
        self.lineEditPrelist = []
        for i in range(1, 20, 1):
            name = "PreLineEdit_" + str(i)
            line = ui.findChild(QLineEdit, name)
            self.lineEditIntralist.append(line)

        #Combo box
        self.comboBoxPrelist = []
        for i in range(1, 8, 1):
            name = "PrecomboBox_" + str(i)
            box = ui.findChild(QComboBox, name)
            self.comboBoxPrelist.append(box)

    def initIntraButtons(self, ui):
        #Line edit
        self.lineEditIntralist = []
        for i in range(1, 18, 1):
            name = "IntraLineEdit_" + str(i)
            line = ui.findChild(QLineEdit, name)
            self.lineEditIntralist.append(line)

        #Combo box
        self.comboBoxIntralist = []
        for i in range(1, 20, 1):
            name = "IntracomboBox_" + str(i)
            box = ui.findChild(QComboBox, name)
            self.comboBoxIntralist.append(box)

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

        box = ui.findChild(QLineEdit, "post1_comboBox")
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

        box = ui.findChild(QLineEdit, "post2_comboBox")
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

        box = ui.findChild(QLineEdit, "post3_comboBox")
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

        box = ui.findChild(QLineEdit, "post4_comboBox")
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

        box = ui.findChild(QLineEdit, "post5_comboBox")
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

        box = ui.findChild(QLineEdit, "post6_comboBox")
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

        box = ui.findChild(QLineEdit, "post7_comboBox")
        self.post7List.append(box)

        dmy = ui.findChild(QDateEdit, "post7_dateEdit")
        self.post7List.append(dmy)






