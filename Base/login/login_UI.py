import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from Base.login import User_Application

class Login_UI(QMainWindow):
    def __init__(self, parent= None):
        QMainWindow.__init__(self, None)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("bg_login.png")))
        self.setPalette(palette)
        self.initUI()

    def initUI(self):
        loader = QUiLoader()
        form = loader.load('./Widget_LoginUI.ui', self)
        self.user_id = form.findChild(QLineEdit, "lineEdit_username")
        self.password = form.findChild(QLineEdit, "lineEdit_password")
        self.login_button = form.findChild(QPushButton, "button_login")
        self.login_button.clicked.connect(self.logIn)

    def logIn(self):
        users = User_Application.User_Application(self.user_id.text(), self.password.text()).user
        print(type(users))
        self.parent.changePageLoginSection("login", users)


def main():
    app = QApplication(sys.argv)
    ui = Login_UI()
    ui.show()
    app.exec_()

if __name__ == "__main__":
    main()