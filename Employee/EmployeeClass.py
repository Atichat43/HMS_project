
class Employee(object):
    def __init__(self, id, username, password, type, firstname, lastname, phone_number):
        self.id = id
        self.username = username
        self.password = password
        self.type = type
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number

    def getData(self):
        text = []
        text.append(self.id)
        text.append(self.username)
        text.append(self.password)
        #text.append(self.type)
        text.append(self.firstname)
        text.append(self.lastname)
        text.append(self.phone_number)
        return text

    def setUsername(self, u):
        self.username = u

    def getUsername(self):
        return self.username

    def setPassword(self, pw):
        self.password = pw

    def getPassword(self):
        return self.password

    def getType(self):
        return self.type
    
    def setId(self, new_id):
        self.id = new_id

    def getId(self):
        return self.id

    def setFirstname(self, new_firstname):
        self.firstName = new_firstname

    def getFirstname(self):
        return self.firstname

    def setLastname(self, new_lastname):
        self.lastname = new_lastname

    def getLastname(self):
        return self.lastname

    def setPhone(self, new_phone_number):
        self.phone_number = new_phone_number

    def getPhone(self):
        return self.phone_number

