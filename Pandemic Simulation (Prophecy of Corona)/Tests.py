from main import *
import unittest
from Repository import *
from Services import *

class Tests(unittest.TestCase):
    

    def test_simulate(self):

        self.assertEqual(s.simulate(),1)

    def test_infect(self):
        self.assertEqual(s.infect(),1)


if __name__ == '__main__':
    unittest.main()

    