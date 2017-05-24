from PySide.QtGui import *

from Base.login import login_UI

class Login_Application(QMainWindow):
    def __init__(self):
        #Main UI set up
        QMainWindow.__init__(self, None)
        self.setMinimumSize(1280, 720)
        self.setWindowTitle("HMS version 1.0.1")

        # Init main Widget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Init state attributes
        self.state = 'Not Login'

        # Add widget
        self.login_widget = login_UI.Login_UI(self)
        self.central_widget.addWidget(self.login_widget)



    # Change page signal (send from log in UI page)
    def changePageLoginSection(self, signal = None, user = None):
        if (signal == "login" and user != None):
            print('login pressed')
            print(type(user))
            self.state = "Login"

        else:
            ### create pop-up
            print('Wrong login')


def main():
    import sys
    app = QApplication(sys.argv)
    ui = Login_Application()
    ui.show()
    app.exec_()

if __name__ == "__main__":
    main()