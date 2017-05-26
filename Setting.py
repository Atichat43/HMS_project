from enum import Enum
#Doctor
#posX posY sizeW sizeH
GEOMETRY_MAINWIDOW = 50, 50, 800, 600
GEOMETRY_DIALOG_NEW_PATIENT = 550, 60, 580, 600
GEOMETRY_DIALOG_3REPORT = 350, 60, 850, 600
GEOMETRY_MSG = []

STATUS = ["Green", "Orange", "Red", "White"]
NUMBER_OF_ROOM = 13

#Manage_Person For ADMIN
HEAD_BAR_DOCTOR = [ "ID", "Username", "Password", "Firstname", "Lastname", "Phone", "Position"]
HEAD_BAR_ROOMMANAGER = ["ID", "Username", "Password", "Firstname", "Lastname", "Phone"]
HEAD_BAR_NURSE = ["ID", "Username", "Password", "Firstname", "Lastname", "Phone"]

#Manage Person For Doctor
HEAD_BAR_PATIENT = ["Date", "Time", "Room", "Pre_Diagnosis", "Plan"]

#path RSC images
PATH_IMG_BG_LOGIN = ".RSC/img/bg_login.png"

#path Doctor
PATH_DOCTOR_DIALOG_NEWPATIENT = 'Employee/Doctor/View/Widget_NewPatientUI.ui'
PATH_DOCTOR_DIALOG_3REPORT = 'Employee/Doctor/View/Widget_3ReportPatientUI.ui'

#path database
DB_USER = "./Database/userObject.pkl"
DB_PATIENT = "./Database/patientObject.pkl"
DB_APPOINTMENT = "./Database/appointmentObject.pkl"

#Style Sheet
SS_Button_EMCASE = "background-color: rgb(255, 0, 0); color: rgb(255, 255, 255)"
SS_TabWidget = "QTabBar::tab { height: 35px; width: 100px; }"

#Enum
class Position(Enum):
    admin = 0
    doctor = 1
    nurse = 2
    roommanager = 3

#ROOM CLASS
"""
STATUS[0] = Free
STATUS[1] = Medium
STATUS[2] = Busy
STATUS[3] = Not available
"""




