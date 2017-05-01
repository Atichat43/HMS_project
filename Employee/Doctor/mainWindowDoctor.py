import sys

from PySide.QtCore import QDateTime, Qt

import ControllerClass
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
from Patient.view import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loader = QUiLoader()
        self.tabWidget = QTabWidget()
        self.centralWidget = QWidget()
        self.initUI()
        self.initButtonTab2()

    def initUI(self):
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("Doctor window")
        self.setTab()
        grid = QGridLayout()
        grid.addWidget(self.tabWidget)
        self.centralWidget.setLayout(grid)
        self.setCentralWidget(self.centralWidget)
        self.show()

    def setTab(self):
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 35px; width: 100px; }")
        self.tab1 = self.loader.load('./view/Tab1_CalendarUI.ui', self)
        self.tab2 = self.loader.load('./view/Tab2_PatientUI.ui', self)
        self.tabWidget.addTab(self.tab1, "Dashboard")
        self.tabWidget.addTab(self.tab2, "Patient")

    def initButtonTab2(self):
        b_newPatient = self.tab2.findChild(QPushButton, "b_newPatient")
        b_newPatient.clicked.connect(self.addNewPatient)

    def addNewPatient(self):
        pass






def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    exit(app.exec_())

if __name__ == "__main__":
    main()
