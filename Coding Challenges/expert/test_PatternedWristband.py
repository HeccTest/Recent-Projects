from patternedWristband import is_wristband
import unittest

# a list of test cases taken from the edabit testing page. I modified the contents to be executable in my use case.

class testingPatternedWristband(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_wristband( 
        [['A', 'A'], 
        ['B', 'B'], 
        ['C', 'C']]), True)

    def test_2(self):
        self.assertEqual(is_wristband(
        [['A', 'B'], 
        ['A', 'B'], 
        ['A', 'B']]), True)

    def test_3(self):
        self.assertEqual(is_wristband(
        [['A', 'B', 'C'], 
        ['C', 'A', 'B'], 
        ['B', 'C', 'A'], 
        ['A', 'B', 'C']]), True)

    def test_4(self):
        self.assertEqual(is_wristband(
        [['A', 'B', 'C'], 
        ['C', 'A', 'B'], 
        ['D', 'C', 'A'], 
        ['E', 'D', 'C']]), True)

    def test_5(self):
        self.assertEqual(is_wristband(
        [['A', 'B', 'C'], 
        ['B', 'A', 'B'], 
        ['D', 'C', 'A'], 
        ['E', 'D', 'C']]), False)

    def test_6(self):
        self.assertEqual(is_wristband(
        [['A', 'B', 'C'], 
        ['B', 'C', 'A'], 
        ['C', 'A', 'B'], 
        ['A', 'B', 'A']]), True)

    def test_7(self):
        self.assertEqual(is_wristband(
        [['A', 'B', 'C'], 
        ['B', 'C', 'D'], 
        ['C', 'D', 'E'], 
        ['D', 'E', 'F']]), True)

    def test_8(self):
        self.assertEqual(is_wristband(
        [['A', 'B', 'C'], 
        ['B', 'C', 'D'], 
        ['C', 'D', 'E'], 
        ['D', 'E', 'E']]), True)

    def test_9(self):
        self.assertEqual(is_wristband(
        [['A', 'B', 'C'], 
        ['B', 'C', 'D'], 
        ['C', 'D', 'E'], 
        ['D', 'F', 'E']]), False)

    def test_10(self):
        self.assertEqual(is_wristband(
        [['A', 'B', 'C'], 
        ['B', 'D', 'A'], 
        ['C', 'A', 'B'], 
        ['A', 'B', 'A']]), False)

    def test_11(self):
        self.assertEqual(is_wristband(
        [['A', 'B'],  
        ['A', 'B'], 
        ['A', 'C'],
        ['A', 'B']]), False)

    def test_12(self):
        self.assertEqual(is_wristband(
        [['A', 'A'],
        ['B', 'B'],
        ['C', 'C'],
        ['D', 'B']]), False)
        
    def test_13(self):
        self.assertEqual(is_wristband(
        [['A', 'A'],
        ['B', 'B'],
        ['C', 'C'],
        ['C', 'C']]), True)


if __name__ == "__main__":
    unittest.main()