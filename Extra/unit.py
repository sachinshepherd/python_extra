import unittest

def sum(a,b):
    return a+b

class MyTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2,3),5)
        self.assertEqual(sum(2,3),6)
    