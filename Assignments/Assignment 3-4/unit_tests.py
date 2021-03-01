from init import students
import unittest
import req1

class Mytest1(unittest.TestCase):
    def test(self):
        self.assertEqual(req1.add(2,2,2),[[3,8,10],[10,10,9],[2,4,8],[3,2,5],[10,10,10],[6,7,8],[4,2,10],[5,2,1],[8,8,8],[6,7,10],[2,2,2]])

class Mytest2(unittest.TestCase):
    def test(self):
        self.assertEqual(req1.insert(2,2,2,2),[[3,8,10],[10,10,9],[2,2,2],[3,2,5],[10,10,10],[6,7,8],[4,2,10],[5,2,1],[8,8,8],[6,7,10]])
