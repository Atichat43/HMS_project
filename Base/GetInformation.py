import psycopg2

class GetInformation():
    def __init__(self, choose):
        self.choose = choose
        if(self.choose == 'doctor'):
            self.sql_select = """SELECT users_username, users_password, doctor_id, doctor_firstname, doctor_lastname, doctor_phone_number, doctor_department
                                 From users u1, doctor d1
                                 WHERE u1.users_id = d1.doctor_id"""
        elif(self.choose == 'nurse'):
            self.sql_select = """SELECT users_username, users_password, nurse_id, nurse_firstname, nurse_lastname, nurse_phone_number
                                 From users u1, nurse n1
                                 WHERE u1.users_id = n1.nurse_id"""
        elif(self.choose == 'roommanager'):
            self.sql_select = """SELECT users_username, users_password, roommanager_id, roommanager_firstname, roommanager_lastname, roommanager_phone_number
                                 From users u1, roommanager r1
                                 WHERE u1.users_id = r1.roommanager_id"""
        else:
            self.sql_select = None

        self.lst = self.getDB(self.sql_select)

    def getDB(self, sql_select):
        lst = []
        try:
            conn_string = "host='localhost' dbname='postgres' user='postgres' password='4141'"
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            cursor.execute(sql_select)
            row = cursor.fetchone()
            while row is not None:
                lst.append(row)
                row = cursor.fetchone()  ##fetchont() return next row of query in type of single tuple or None
            cursor.close()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()
        return lst

