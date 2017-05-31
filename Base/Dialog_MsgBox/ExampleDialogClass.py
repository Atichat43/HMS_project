from PySide.QtCore import QRegExp, QPoint
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader

from Base.Dialog_MsgBox import ConfirmMsgClass

class ExampleDialog(QDialog):
    def __init__(self, parent = None):
        super(ExampleDialog, self).__init__(parent)
        self.setGeometry(300,200,400,400)
        self.loader = QUiLoader()
        self.ui = self.loader.load('./widgetTestDialog.ui', self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.ui)
        self.initUI()

        #Line Edit with QDoubleValidator must be int
        self.l = QLineEdit()
        validator = QDoubleValidator()
        self.l.setValidator(validator)
        self.l.textChanged.connect(self.check_state)
        self.l.textChanged.emit(self.l.text())
        self.layout.addWidget(self.l)
        self.show()

    def check_state(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if state == QValidator.Acceptable:
            color = '#c4df9b'  # green
        elif state == QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def initUI(self):
        self.setInput1 = []
        self.setInput1.append(self.ui.findChild(QLineEdit, "lineEdit_1"))
        self.setInput1.append(self.ui.findChild(QLineEdit, "lineEdit_2"))
        self.setInput1.append(self.ui.findChild(QLineEdit, "lineEdit_3"))

        self.b_save = self.ui.findChild(QPushButton, "b_save")
        self.b_discard = self.ui.findChild(QPushButton, "b_discard")
        self.b_save.clicked.connect(self.save)
        self.b_discard.clicked.connect(self.discard)


    def onTextChange(self, text):
        regExp = QRegExp()
        regExp.setPattern("[^0-9]*")
        m_correctText = ""
        if regExp.exactMatch(text):
            m_correctText = text
            QToolTip.hideText()

        else:
            point = QPoint(self.l.geometry().left(), self.l.geometry().bottom())
            self.l.setText(m_correctText)
            QToolTip.showText(point, "Cannot enter number..")

    def save(self):
        self.ans = []
        for i in range(len(self.setInput1)):
            self.ans.append(self.setInput1[i].text())
        print(self.ans)
        return True

    def discard(self):
        dialog = ConfirmMsgClass.ConfirmYesNo()
        if dialog.ans == True:
            print("Discard")
            self.close()
        else:
            print("Cancel")
