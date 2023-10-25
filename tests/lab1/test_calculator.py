import unittest
import sys
from src.lab1.calculator import calculate

class Test(unittest.TestCase):
        def test_one(self):
                self.assertEqual(calculate(1,2, '+'), 3)
                self.assertEqual(calculate(1,2, '-'), -1)
                self.assertEqual(calculate(1,2, '*'), 2)
                self.assertEqual(calculate(1,2, '/'), 0.5)
                self.assertEqual(calculate(1,2, 'Сори за пропущенный дедлайн:(((((('), 'ERROR')
                self.assertEqual(calculate('Еще раз сори',2, '+'), 'ERROR')
                self.assertEqual(calculate(1,'И закрепительный сорян', '+'), 'ERROR')

                


if __name__ == "__main__":
         unittest.main()
