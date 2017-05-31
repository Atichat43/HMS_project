from enum import Enum

# GEOMETRY posX posY sizeW sizeH
GEOMETRY_MAINWIDOW = 50, 50, 800, 600
GEOMETRY_DIALOG_NEW_PATIENT = 550, 60, 580, 600
GEOMETRY_DIALOG_3REPORT = 350, 60, 755, 550
GEOMETRY_DIALOG_NEW_EMPLOYEE = 300, 200, 300, 230
GEOMETRY_DIALOG_HISTORY_REPORT = 400, 100, 900, 600
GEOMETRY_MSG = []

# STATUS = ["Green", "Orange", "Red", "White"]
NUMBER_OF_ROOM = 13

# Manage_Person For ADMIN
HEAD_BAR_DOCTOR = ["ID", "Username", "Password", "Firstname", "Lastname", "Phone", "Position"]
HEAD_BAR_ROOMMANAGER = ["ID", "Username", "Password", "Firstname", "Lastname", "Phone"]
HEAD_BAR_NURSE = ["ID", "Username", "Password", "Firstname", "Lastname", "Phone"]
HEAD_BAR_ADMIN = ["ID", "Username", "Password", "Firstname", "Lastname", "Phone"]

# Manage Person For Doctor
HEAD_BAR_PATIENT = ["Case_id", "Date", "Time", "Room", "Name", "Pre_Diagnosis", "Plan"]
HB_DOCTOR_PATIENT = ["AN", "Name", "Age", "Phone"]

# Manage Person For RoomManager
HEAD_BAR_APPOINTMENT = ["Case_id", "Data", "Time", "Doctor", "Patient", "Status"]

# Manage Person For Nurse
HB_NURSE_PATIENT = ["AN", "Name", "Age", "Phone", "Status"]

# path RSC images
PATH_IMG_BG_LOGIN = ".RSC/img/bg_login.png"

"""-------PATH UI FILE--------"""
# path Doctor
PATH_DOCTOR_DIALOG_NEWPATIENT = 'Employee/Doctor/View/Widget_NewPatientUI.ui'

# ../Employee/Doctor/View/Widget_3ReportPatientUI.ui
PATH_DOCTOR_DIALOG_3REPORT = 'Employee/Doctor/View/Widget_3ReportPatientUI.ui'


"""-------PATH DATABASE FILE--------"""
# path database
DB_USER = "./Database/userObject.pkl"
DB_PATIENT = "./Database/patientObject.pkl"
DB_APPOINTMENT = "./Database/appointmentObject.pkl"
DB_REPORT = "./Database/reportObject.pkl"


"""--------STYLE SHEET------------"""
# Style Sheet
SS_Button_EMCASE = "background-color: rgb(255, 0, 0); color: rgb(255, 255, 255)"
SS_TabWidget = "QTabBar::tab { height: 35px; width: 100px; }"


# Appointment
class Status(Enum):
    waiting = 0
    doing = 1
    done = 2

# Calendar
class Month(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Juy = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12


# Paitient
class PatientStatus(Enum):
    waitingPreReport = 0
    waitingIntraReport = 1
    waitingPostReport = 2
    done = 3


class Position(Enum):
    admin = 0
    doctor = 1
    nurse = 2
    roommanager = 3


class UserPosition(Enum):
    doctor = 0
    nurse = 1
    admin = 2


class NewObjectReturnVal(Enum):
    exist = 0
    created = 1
    wrong_input = 2


class EditObjectReturnVal(Enum):
    not_found = 0
    edited = 1
