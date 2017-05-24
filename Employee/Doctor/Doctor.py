from PySide.QtGui import QMainWindow, QGridLayout, QWidget, QTabWidget
from Employee.Doctor import Tab1_CalendarClass, Tab2_PatientClass
import Setting


class MainWindowDoctor(QMainWindow):
    def __init__(self):
        super(MainWindowDoctor, self).__init__()
        self.initUI()
        self.initLayout()

    def initUI(self):
        posX, posY, sizeW, sizeH = Setting.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.setWindowTitle("Doctor window")
        self.setTab()
        self.show()

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tabWidget)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def setTab(self):
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet(Setting.SS_TabWidget)
        self.tab1 = Tab1_CalendarClass.Tab1Calendar()
        self.tab2 = Tab2_PatientClass.Tab2Patient()
        self.tabWidget.addTab(self.tab1, "Dashboard")
        self.tabWidget.addTab(self.tab2, "Patient")

if __name__ == "__main__":
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    win = MainWindowDoctor()
    exit(app.exec_())
