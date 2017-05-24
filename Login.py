from PySide.QtGui import QMainWindow, QGridLayout, QWidget, QPalette, QBrush, QPixmap, QLineEdit, QPushButton
from PySide.QtUiTools import QUiLoader
from Base.Dialog_MsgBox import ConfirmMsgClass
import Setting as s
import Login_System


class LoginWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.system = Login_System.LoginSystem()
        self.initUI()
        self.initButton()
        self.show()

    def initUI(self):
        posX, posY, sizeW, sizeH = s.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.setWindowTitle("Hospital Management System")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(s.PATH_IMG_BG_LOGIN)))
        self.setPalette(palette)
        self.initButton()

    def initButton(self):
        loader = QUiLoader()
        form = loader.load('RSC/loginUI/Widget_LoginUI.ui', self)
        self.user_id = form.findChild(QLineEdit, "lineEdit_username")
        self.password = form.findChild(QLineEdit, "lineEdit_password")
        self.login_button = form.findChild(QPushButton, "button_login")
        self.login_button.clicked.connect(self.logIn)

    def initLayout(self):
        layout = QGridLayout()
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def logIn(self):
        # user_name, psw = self.user_id.text(), self.password.text()
        # found, user, position = self.system.checkRegisteredUser(user_name, psw)
        # if not found:
        #     dialog = ConfirmMsgClass.ConfirmYesNo()
        #     dialog.show()
        #     dialog.exec_()
        #     self.clear()
        self.parent.loginSucess(3)
        self.close()

    def clear(self):
        self.user_id.clear()
        self.password.clear()


