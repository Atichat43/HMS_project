from PySide.QtCore import QRegExp
from PySide.QtGui import *


class AllLineEdit(QDialog):
    def __init__(self, parent = None):
        super(AllLineEdit, self).__init__(parent)
        self.setGeometry(300, 200, 400, 400)

        self.lineEdit_QDoubleValiator = QLineEdit()
        self.lineEdit_CheckTying_int = QLineEdit()
        self.lineEdit_CheckTying_text = QLineEdit()

        self.initLineEdit()
        self.addLineEditToLayout()
        self.show()

    def addLineEditToLayout(self):
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.lineEdit_QDoubleValiator)
        self.layout.addWidget(self.lineEdit_CheckTying_int)
        self.layout.addWidget(self.lineEdit_CheckTying_text)

    def initLineEdit(self):
        validator = QDoubleValidator()
        self.lineEdit_QDoubleValiator.setValidator(validator)

        validator = QIntValidator()
        self.lineEdit_CheckTying_int.setValidator(validator)
        self.lineEdit_CheckTying_int.textChanged.connect(self.check_state)
        self.lineEdit_CheckTying_int.textChanged.emit(self.lineEdit_CheckTying_int.text())

        regExp = QRegExp('[A-C]\\d{5}[W-Z]')
        validator = QRegExpValidator(regExp)
        self.lineEdit_CheckTying_text.setValidator(validator)
        self.lineEdit_CheckTying_text.textChanged.connect(self.check_state)
        self.lineEdit_CheckTying_text.textChanged.emit(self.lineEdit_CheckTying_text.text())

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
