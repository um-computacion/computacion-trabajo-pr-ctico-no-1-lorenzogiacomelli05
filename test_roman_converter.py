import unittest
from roman_converter import decimal_a_romano

class TestDecimalARomano(unittest.TestCase):
    
    def test_basicos(self):
        self.assertEqual(decimal_a_romano(1), "I")
        self.assertEqual(decimal_a_romano(5), "V")
        self.assertEqual(decimal_a_romano(10), "X")
        self.assertEqual(decimal_a_romano(50), "L")
        self.assertEqual(decimal_a_romano(100), "C")
        self.assertEqual(decimal_a_romano(500), "D")
        self.assertEqual(decimal_a_romano(1000), "M")
    def test_substraction(self):
        self.assertEqual(decimal_a_romano(4), "IV")
        self.assertEqual(decimal_a_romano(9), "IX")
        self.assertEqual(decimal_a_romano(40), "XL")
        self.assertEqual(decimal_a_romano(90), "XC")
        self.assertEqual(decimal_a_romano(400), "CD")
        self.assertEqual(decimal_a_romano(900), "CM")
    def test_combinations(self):
        self.assertEqual(decimal_a_romano(44), "XLIV")
        self.assertEqual(decimal_a_romano(99), "XCIX")
        self.assertEqual(decimal_a_romano(444), "CDXLIV")
        self.assertEqual(decimal_a_romano(999), "CMXCIX")
        self.assertEqual(decimal_a_romano(1987), "MCMLXXXVII")

if __name__ == "__main__":
   unittest.main()