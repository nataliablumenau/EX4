

from firebase import firebase
import md5

FIREBASE_URL = r'https://moodle-96c01.firebaseio.com/'

class DataManager():
    def __init__(self, repo_url):
        self.URL = repo_url
        self.fb = firebase.FirebaseApplication(self.URL, None)
        
    def getUsername(self, username):
        return self.fb.get('/users/',username)
        
    def getAllUsers(self):
        return self.fb.get('/users/',None)
    
    def removeAll(self):
        self.fb.delete('/','users')
        
    def deleteUser(self, username):
        self.fb.delete('/users/',username)
        
    def addNewUser(self, username, password):
        return self.fb.patch('/users', { username : { "username" : username , "password" : md5.new(password).hexdigest()}})
        
    def setUserDetails(self, username, account_number, name, courses):
        return self.fb.patch('/users/'+username, { "accountNumber": account_number,"fullName" : name , "courses" : courses})
        
class InputOutput():
    def __init__(self):
        pass
        
    def takeInput(self, msg):
        return raw_input(msg)
        
class CLI():
    def __init__(self, io, fb):
        self.io = io
        self.fb = fb
        
    def checkUser(self):
        username = self.io.takeInput("Enter username:")
        result = self.fb.getUsername(username)
        return result is not None

    def showUsers(self):
        result = self.fb.getAllUsers()
        print "-----------------------------"
        if result:
            print "Username".ljust(20)+"Password (hash)".ljust(40)
            for v in result.values():
                print v['username'].ljust(20)+v['password'].ljust(40)
        else:
            print "No users" 
        print "-----------------------------"

    def removeUser(self):
        username = self.io.takeInput("Enter username:")
        result = self.fb.getUsername(username)
        if not result:
            print "-----------------------------"
            print "ERROR: The username does not exist"
            print "-----------------------------"
            return False
        self.fb.deleteUser(username)
        result = self.fb.getUsername(username)
        return not result

    def addUser(self):
        username = self.io.takeInput("Enter username:")
        result = self.fb.getUsername(username)
        if result:
            print "-----------------------------"
            print "ERROR: The username is already exist"
            print "-----------------------------"
            return

        password = self.io.takeInput("Enter password:")
        result = self.fb.addNewUser(username, password)        
        print "-----------------------------"
        if result:
            print "The user "+result.keys()[0]+" has been added succesfuly"
        else:
            print "ERROR: Add user failed, please try again"
        print "-----------------------------"
        
    def execute(self):
        cmd = self.io.takeInput("Enter command:\n")
        if cmd == "add user":
            self.addUser()
        elif cmd == "remove user":
            self.removeUser()
        elif cmd == "show users":
            self.showUsers()
        elif cmd == "check user":
            result = self.checkUser()            
            print "-----------------------------"
            if result:
                print "EXIST"
            else:
                print "DOES NOT EXIST"
            print "-----------------------------"
        elif cmd == "remove all":
            self.fb.removeAll()
        elif cmd == "set details":
            self.setUserDetails()
        elif cmd == "exit":
            return False
        else:
            print "Invalid command"
        return True
    

    def setUserDetails(self):
        username = self.io.takeInput("Enter username:")
        result = self.fb.getUsername(username)
        if not result:
            print "-----------------------------"
            print "ERROR: The username does not exist"
            print "-----------------------------"
            return

        name = self.io.takeInput("Enter full name:")
        account_number = self.io.takeInput("Enter account number:")
        while not account_number.isdigit():
            print "ERROR: Account number must be a number"
            account_number = self.io.takeInput("Enter account number:")
        courses = []
        i = 1
        course = self.io.takeInput("Enter course number #"+str(i)+" (ENTER to finish): ")
        while course:
            i+=1
            courses.append(course)
            course = self.io.takeInput("Enter course number #"+str(i)+" (ENTER to finish): ")

        print "-----------------------------"
        print username
        print account_number
        print courses
        print "-----------------------------"

        result = self.fb.setUserDetails(username,account_number,name,courses)
        if result:
            print "User "+result.keys()[0]+" details has been set succesfuly"
        else:
            print "ERROR: Set user details failed, please try again"

    def printMenu(self):
        print "========================================="
        print "================ Commands ==============="
        print "========================================="
        print "add user             add a new user"
        print "remove user          remove a new user"
        print "show users           print all the users"
        print "check user           check if user exist"
        print "remove all           remove all the users"
        print "set details          set additional details for user"
        print "exit                 exit program"
        print "========================================="

def main():
    io = InputOutput()
    fb = DataManager(FIREBASE_URL)
    cli = CLI(io, fb)
    res = True
    while res:
        cli.printMenu()
        res = cli.execute()

if __name__ == "__main__":
    main()