'''
Test Module

'''
from Domain import *
from main import *
import UI
from Services import *
from Repository import *
import unittest


class Tests(unittest.TestCase): #Test class which tests the first functionalities

    def test_addStudent(self):
        snew=Student("11","Mario","5",assig1)
        self.assertEqual(s.s_repo.addStudent(snew),snew)


    def test_removeStudent(self):
        self.assertEqual(s.s_repo.removeStudent("11"),s10)

    def test_updateStudent(self):

        snew=Student("9","Mario","5",assig1)
        self.assertEqual(s.s_repo.updateStudent(snew),snew)

    def test_addAssignment(self):
        assignew=Assignment("6","Assignment 6",datetime.date(2019,11,16))
        self.assertEqual(s.assig_repo.addAssignment(assignew),assignew)

    def test_removeAssignment(self):
        self.assertEqual(s.assig_repo.removeAssignment("6"),assig5)

    def test_updateAssignment(self):

        assignew=Assignment("4","Assignment 4 New",datetime.date(2019,11,16))
        self.assertEqual(s.assig_repo.updateAssignment(assignew),assignew)












if __name__ == '__main__':
    unittest.main()