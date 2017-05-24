import psycopg2
from PySide.QtGui import *
from Base.ManagePerson import Widget_ManagePersonClass
import Setting


class MainWindowAdmin(QMainWindow):
    def __init__(self):
        super(MainWindowAdmin, self).__init__()
        self.initUI()
        self.initLayout()

    def initUI(self):
        posX, posY, sizeW, sizeH = Setting.GEOMETRY_MAINWIDOW
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.setWindowTitle("Admin Main Window")
        self.setTab()
        self.show()

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.tabWidget)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def setTab(self):
        # allRowDatabaseDoctor = getDoctorDB()
        # allRowDatabaseNurse = getNurseDB()
        # allRowDatabaseRoom = getRoomDB()
        allRowDatabaseDoctor = []
        allRowDatabaseNurse = []
        allRowDatabaseRoom = []
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet(Setting.SS_TabWidget)
        self.tab1 = Widget_ManagePersonClass.WidgetManagePerson("Doctor")
        self.tab1.setSourceModel(Setting.HEAD_BAR_DOCTOR, allRowDatabaseDoctor)
        self.tab2 = Widget_ManagePersonClass.WidgetManagePerson("Nurse")
        self.tab2.setSourceModel(Setting.HEAD_BAR_NURSE, allRowDatabaseNurse)
        self.tab3 = Widget_ManagePersonClass.WidgetManagePerson("Room manager")
        self.tab3.setSourceModel(Setting.HEAD_BAR_ROOMMANAGER, allRowDatabaseRoom)
        self.tabWidget.addTab(self.tab1, "Doctor")
        self.tabWidget.addTab(self.tab2, "Nurse")
        self.tabWidget.addTab(self.tab3, "RoomManager")


def getDoctorDB():
    lst = []
    sql_select = """SELECT users_username, users_password, doctor_id from users"""
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()
        while row is not None:
            if(row[2] != None):
                lst.append(row)
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

    sql_select = """SELECT * from doctor"""
    new_lst = []
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()
        count = 0
        while row is not None:
            for tup in lst:
                if(tup[2] == row[0]):
                    new_lst.append((lst[count][0], lst[count][1], row[0], row[1], row[2], row[3], row[4]))
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
    return new_lst

def getNurseDB():
    lst = []
    sql_select = """SELECT users_username, users_password, nurse_id from users"""
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()

        while row is not None:
            if (row[2] != None):
                lst.append(row)
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

    sql_select = """SELECT * from nurse"""
    new_lst = []
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()
        count = 0
        while row is not None:
            for tup in lst:
                if(tup[2] == row[0]):
                    new_lst.append((lst[count][0], lst[count][1], row[0], row[1], row[2], row[3]))
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
    return new_lst

def getRoomDB():
    lst = []
    sql_select = """SELECT users_username, users_password, roommanager_id from users"""
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()

        while row is not None:
            if (row[2] != None):
                lst.append(row)
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

    sql_select = """SELECT * from roommanager"""
    new_lst = []
    try:
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        row = cursor.fetchone()
        count = 0
        while row is not None:
            for tup in lst:
                if(tup[2] == row[0]):
                    new_lst.append((lst[count][0], lst[count][1], row[0], row[1], row[2], row[3]))
            row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
    return new_lst


def main():
    import sys
    app = QApplication(sys.argv)
    win = MainWindowAdmin()
    exit(app.exec_())


if __name__ == "__main__":
    main()
