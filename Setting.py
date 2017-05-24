from enum import Enum
#ROOM CLASS
"""
STATUS[0] = Free
STATUS[1] = Medium
STATUS[2] = Busy
STATUS[3] = Not available
"""

#Doctor
#posX posY sizeW sizeH
GEOMETRY_MAINWIDOW = 50, 50, 800, 600
GEOMETRY_DIALOG_NEW_PATIENT = 550, 60, 580, 600
GEOMETRY_DIALOG_3REPORT = 350, 60, 850, 600
GEOMETRY_MSG = []

STATUS = ["Green", "Orange", "Red", "White"]
NUMBER_OF_ROOM = 13

HEAD_BAR_DOCTOR = ["Username", "Password", "ID", "Firstname", "Lastname", "Phone", "Position"]
HEAD_BAR_ROOMMANAGER = ["Username", "Password", "ID", "Firstname", "Lastname", "Phone"]
HEAD_BAR_NURSE = ["Username", "Password", "ID", "Firstname", "Lastname", "Phone"]
HEAD_BAR_PATIENT = ["NAME", "ID", "Position", "Phone"]



#Style Sheet
SS_Button_EMCASE = "background-color: rgb(255, 0, 0); color: rgb(255, 255, 255)"
SS_TabWidget = "QTabBar::tab { height: 35px; width: 100px; }"


#path RSC images
PATH_IMG_BG_LOGIN = "RSC/img/bg_login.png"

#Database
#User Table
# class TableUser(Enum):
#     username = 0
#     psw = 1
#     position = 2
DB_USER = "userObject.pkl"

#Position
class Position(Enum):
    admin = 0
    doctor = 1
    nurse = 2
    roomManager = 3




