from entro import calculate_entropy
import unittest

class test_calculations(unittest.TestCase):
    def calculates_entropy(self):
        rounded_entropy = round(calculate_entropy(2, 3), 5)
        self.assertEqual(rounded_entropy, 0.97095)

if __name__ == '__main__':
    unittest.main(exit=False)
