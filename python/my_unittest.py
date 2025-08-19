import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)  
        self.assertEqual(add(-1, 1), 0) 
        self.assertNotEqual(add(2, 2), 5) 

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertNotEqual(subtract(10, 2), 5)

if __name__ == '__main__':
    unittest.main()

# create calculator.py file and check using    python -m unittest my_unittest.py