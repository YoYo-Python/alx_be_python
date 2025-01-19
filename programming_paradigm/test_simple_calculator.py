import unittest
from simple_calculator import SimpleCalculator

class Operation(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1),0)
        self.assertEqual(self.calc.add(-1000,1),-999)
        self.assertEqual(self.calc.add(10000000,100),10000100)
        self.assertEqual(self.calc.add(5,1),6)        
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,3),-1)
        self.assertEqual(self.calc.subtract(-1,1),-2)
        self.assertEqual(self.calc.subtract(-1000,1),-1001)
        self.assertEqual(self.calc.subtract(1999,100),1899)
        self.assertEqual(self.calc.subtract(5,1),4)

    def test_division(self):
        self.assertEqual(self.calc.divide(2,3),2/3)
        self.assertEqual(self.calc.divide(1,10),0.1)
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertEqual(self.calc.divide(9,3),3)
        self.assertEqual(self.calc.divide(5,0),None) 
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,3),6)
        self.assertEqual(self.calc.multiply(1,10),10)
        self.assertEqual(self.calc.multiply(4,2),8)
        self.assertEqual(self.calc.multiply(9,3),27)
        self.assertEqual(self.calc.multiply(5,0),0) 
    


