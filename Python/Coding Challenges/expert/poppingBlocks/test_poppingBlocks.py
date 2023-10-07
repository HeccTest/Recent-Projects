from poppingBlocks import final_result
import unittest

# a list of test cases taken from the edabit testing page. I modified the contents to be executable in my use case.

class testingPoppingBlocks(unittest.TestCase):

    def test_1(self):
        self.assertEqual(final_result(['B', 'B', 'A', 'C', 'A', 'A', 'C']), ['A'])

    def test_2(self):
        self.assertEqual(final_result(['B', 'B', 'C', 'C', 'A', 'A', 'A']), [])

    def test_3(self):
        self.assertEqual(final_result(['C', 'A', 'C']), ['C', 'A', 'C'])

    def test_4(self):
        self.assertEqual(final_result(['C', 'A', 'A', 'C', 'B']), ['B'])

    def test_5(self):
        self.assertEqual(final_result(['C', 'C']), [])

    def test_6(self):
        self.assertEqual(final_result(['A', 'B', 'C', 'C', 'B', 'D', 'A']), ['A', 'D', 'A'])

    def test_7(self):
        self.assertEqual(final_result(['A', 'B', 'A', 'A', 'A', 'B', 'B']), ['A'])

if __name__ == "__main__":
    unittest.main()