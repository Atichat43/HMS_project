from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
from Employee.Roommanager import RoomSystemClass
import Setting

class Tab1AllRoom(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()
        self.initLayout()
        self.initButton()
        self.initConnect()

    def initUI(self):
        #path = 'Employee/Roommanager/View/Tab1_AllRoomUI.ui'
        path = './View/Tab1_AllRoomUI.ui'
        self.tab1 = QUiLoader().load(path, self)

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tab1)
        self.setLayout(layout)

    def initButton(self):
        text = "Case no: " + "" + chr(10) \
               + "Doctor: " + "" + chr(10) \
               + "Patient: " + ""
        self.allRoomButton = []
        self.allRoomButton.append(self.tab1.findChild(QPushButton, "buffer"))
        for i in range(1, Setting.NUMBER_OF_ROOM + 1):
            name_room = "room_" + str(i)
            button = self.tab1.findChild(QPushButton, name_room)
            button.setText(text)
            button.setStyleSheet("Text-align:left; Font:12px")
            self.allRoomButton.append(button)
        self.updateRoomUI(1, "0001", "Atichat", "Tiger")

    def initConnect(self):
        self.system = RoomSystemClass.RoomSystem()
        self.allRoomButton[1].clicked.connect(lambda: self.system.getDataOfRoom(1))
        self.allRoomButton[2].clicked.connect(lambda: self.system.getDataOfRoom(2))
        self.allRoomButton[3].clicked.connect(lambda: self.system.getDataOfRoom(3))
        self.allRoomButton[4].clicked.connect(lambda: self.system.getDataOfRoom(4))
        self.allRoomButton[5].clicked.connect(lambda: self.system.getDataOfRoom(5))
        self.allRoomButton[6].clicked.connect(lambda: self.system.getDataOfRoom(6))
        self.allRoomButton[7].clicked.connect(lambda: self.system.getDataOfRoom(7))
        self.allRoomButton[8].clicked.connect(lambda: self.system.getDataOfRoom(8))
        self.allRoomButton[9].clicked.connect(lambda: self.system.getDataOfRoom(9))
        self.allRoomButton[10].clicked.connect(lambda: self.system.getDataOfRoom(10))
        self.allRoomButton[11].clicked.connect(lambda: self.system.getDataOfRoom(11))
        self.allRoomButton[12].clicked.connect(lambda: self.system.getDataOfRoom(12))
        self.allRoomButton[13].clicked.connect(lambda: self.system.getDataOfRoom(13))

    def updateRoomUI(self, NRoom, CaseNo, DName, PName):
        text = "Case no:  " + CaseNo + chr(10) \
               + "Doctor:   " + DName + chr(10) \
               + "Patient:   " + PName
        self.allRoomButton[NRoom].setText(text)

    def updateStatus(self, NRoom, Status):
        pass

    def getAlert(self, NRoom):
        pass

if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication

    app = QApplication(sys.argv)
    tab1_widget = Tab1AllRoom()
    tab1_widget.show()
    sys.exit(app.exec_())
