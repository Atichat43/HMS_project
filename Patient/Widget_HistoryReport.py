from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
import Setting as s
from Base.Dialog_MsgBox import ConfirmMsgClass

class WidgetHistoryReport(QWidget):
    def __init__(self, part_prepre, part_pre, part_intra, part_post):
        QWidget.__init__(self, None)
        posX, posY, sizeW, sizeH = s.GEOMETRY_DIALOG_HISTORY_REPORT
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.part_prepre = part_prepre
        self.part_pre = part_pre
        self.part_intra = part_intra
        self.part_post = part_post
        ## init
        self.initUI()
        self.initLayout()
        self.initPrelabel()
        self.initIntralabel()
        self.initPostlabel()
        ## set data
        self.setPreData()
        self.setIntraData()
        self.setPostData()
        self.show()

    def initUI(self):
        self.loader = QUiLoader()
        self.ui = self.loader.load('./Patient/view/Widget_HistoryReport.ui', self)
        self.b_cancel = self.ui.findChild(QPushButton, "b_cancel")
        self.b_cancel.clicked.connect(self.cancel)

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

    def initPrelabel(self):
        self.labelPrelist = []
        for i in range(1, 41, 1):
            name = "pre_label_" + str(i)
            label = self.ui.findChild(QLabel, name)
            self.labelPrelist.append(label)

    def setPreData(self):
        textPre = self.part_prepre
        textPre += self.part_pre.getHistory()
        count = 0
        for i in self.labelPrelist:
            i.setText(textPre[count])
            i.setStyleSheet("QLabel { background-color : #CCE5FF }")
            count += 1

    def initIntralabel(self):
        self.labelIntralist = []
        for i in range(1, 34, 1):
            name = "intra_label_" + str(i)
            label = self.ui.findChild(QLabel, name)
            self.labelIntralist.append(label)

    def setIntraData(self):
        textIntra = self.part_intra.getHistory()
        count = 0
        for i in self.labelIntralist:
            i.setText(textIntra[count])
            i.setStyleSheet("QLabel { background-color : #FFFFCC }")
            count += 1

    def initPostlabel(self):
        self.labelPostlist = []
        for i in range(1, 34, 1):
            name = "post_label_" + str(i)
            label = self.ui.findChild(QLabel, name)
            self.labelPostlist.append(label)

    def setPostData(self):
        textPost = self.part_post.getHistory()
        count = 0
        for i in self.labelPostlist:
            i.setText(textPost[count])
            i.setStyleSheet("QLabel { background-color : #FFCCCC }")
            count += 1

    def cancel(self):
        self.close()

