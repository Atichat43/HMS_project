from PySide.QtGui import QMainWindow, QGridLayout, QWidget, QTabWidget
from Employee.Roommanager import Tab1_AllRoomClass, Tab2_ManagePatientClass
import Setting


class MainWindowRoomManager(QMainWindow):
    def __init__(self):
        super(MainWindowRoomManager, self).__init__()
        self.initUI()
        self.initLayout()

    def initUI(self):
        posX, posY, sizeW, sizeH = Setting.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.setWindowTitle("RoomManager Main Window")
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
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 35px; width: 100px; }")
        self.tab1 = Tab1_AllRoomClass.Tab1AllRoom()
        self.tab2 = Tab2_ManagePatientClass.Tab2ManagePatient()
        self.tabWidget.addTab(self.tab1, "Manage Room")
        self.tabWidget.addTab(self.tab2, "Patient")

if __name__ == "__main__":
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    win = MainWindowRoomManager()
    exit(app.exec_())
