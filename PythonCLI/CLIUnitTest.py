import unittest
from CLI import CLI

class DummyInputOutput():
    def __init__(self):
        pass
        
    def takeInput(self, msg):
        return "a"

class DummyDataManager():
    def __init__(self):
        self.users = ["a"]
        
    def getUsername(self, username):
        return username in self.users
        
    def deleteUser(self, username):
        if username not in self.users:
            return False
        self.users.remove(username)
        return True
        
class TestCLIMethods(unittest.TestCase):
    def test_checkUser(self):
        io=DummyInputOutput()
        dm=DummyDataManager()
        cli = CLI(io, dm)
        result = cli.checkUser()
        self.assertEqual(result, True)

    def test_removeUser(self):
        io=DummyInputOutput()
        dm=DummyDataManager()
        cli = CLI(io, dm)
        result = cli.removeUser()
        self.assertEqual(result, True)
        self.assertEqual(dm.users, [])

if __name__ == '__main__':
    unittest.main()