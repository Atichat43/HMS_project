import sys
from PySide.QtGui import *

class ConfirmYesNo(QDialog):
    def __init__(self, title="Confirm", textInfo="", question="Do you want to discard your information?"):
        super(ConfirmYesNo, self).__init__(None)
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(textInfo)
        msgBox.setInformativeText(question)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        layout = QGridLayout()
        layout.addWidget(msgBox)
        self.setLayout(layout)
        self.setModal(True)
        self.show()
        choose = msgBox.exec()
        if choose == QMessageBox.Yes:
            self.ans = True
        else:
            self.ans = False
        self.close()


def main():
    app = QApplication(sys.argv)
    win = ConfirmYesNo()
    exit(app.exec_())

if __name__ == "__main__":
    main()