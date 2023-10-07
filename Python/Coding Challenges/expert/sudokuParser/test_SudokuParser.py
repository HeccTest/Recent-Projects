from sudokuParser import Sudoku

import unittest

class testingSudokuParser(unittest.TestCase):

    def testCase1(self):
        self.g1 = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
        self.assertEqual(self.g1.board(), [[4, 1, 7, 9, 5, 0, 0, 3, 0], [0, 0, 0, 0, 0, 0, 7, 0, 0], [0, 6, 0, 0, 0, 7, 0, 0, 0], [0, 5, 0, 0, 0, 9, 1, 0, 6], [8, 0, 0, 6, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3, 4, 0, 0], [9, 0, 0, 0, 0, 5, 0, 0, 0], [0, 0, 0, 4, 3, 0, 0, 0, 0], [2, 0, 0, 7, 0, 1, 5, 8, 0]], "Example Sudoku")
        self.assertEqual(self.g1.get_row(0), [4, 1, 7, 9, 5, 0, 0, 3, 0], "Example Sudoku")
        self.assertEqual(self.g1.get_col(8), [0, 0, 0, 6, 0, 0, 0, 0, 0], "Example Sudoku")
        self.assertEqual(self.g1.get_sqr(1), [9, 5, 0, 0, 0, 0, 0, 0, 7], "Example Sudoku")
        self.assertEqual(self.g1.get_sqr(1, 8), [0, 3, 0, 7, 0, 0, 0, 0, 0], "Example Sudoku")
        self.assertEqual(self.g1.get_sqr(8, 3), [0, 0, 5, 4, 3, 0, 7, 0, 1], "Example Sudoku")

    def testCase2(self):
        self.g2 = Sudoku("005001000287369100416520000000700692000000000000806453843000000000930000950074200")
        self.assertEqual(self.g2.board(), [[0, 0, 5, 0, 0, 1, 0, 0, 0], [2, 8, 7, 3, 6, 9, 1, 0, 0], [4, 1, 6, 5, 2, 0, 0, 0, 0], [0, 0, 0, 7, 0, 0, 6, 9, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 8, 0, 6, 4, 5, 3], [8, 4, 3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 9, 3, 0, 0, 0, 0], [9, 5, 0, 0, 7, 4, 2, 0, 0]])
        self.assertEqual(self.g2.get_row(6), [8, 4, 3, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.g2.get_col(2), [5, 7, 6, 0, 0, 0, 3, 0, 0])
        self.assertEqual(self.g2.get_sqr(2), [0, 0, 0, 1, 0, 0, 0, 0, 0])
        self.assertEqual(self.g2.get_sqr(5, 2), [0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.g2.get_sqr(8, 0), [8, 4, 3, 0, 0, 0, 9, 5, 0])

    def testCase3(self):
        self.g3 = Sudoku("270981006015726983869000271092678354057134829384259617730800462028407130040302798")
        self.assertEqual(self.g3.board(), [[2, 7, 0, 9, 8, 1, 0, 0, 6], [0, 1, 5, 7, 2, 6, 9, 8, 3], [8, 6, 9, 0, 0, 0, 2, 7, 1], [0, 9, 2, 6, 7, 8, 3, 5, 4], [0, 5, 7, 1, 3, 4, 8, 2, 9], [3, 8, 4, 2, 5, 9, 6, 1, 7], [7, 3, 0, 8, 0, 0, 4, 6, 2], [0, 2, 8, 4, 0, 7, 1, 3, 0], [0, 4, 0, 3, 0, 2, 7, 9, 8]])
        self.assertEqual(self.g3.get_row(3), [0, 9, 2, 6, 7, 8, 3, 5, 4])
        self.assertEqual(self.g3.get_col(6), [0, 9, 2, 3, 8, 6, 4, 1, 7])
        self.assertEqual(self.g3.get_sqr(3), [0, 9, 2, 0, 5, 7, 3, 8, 4])
        self.assertEqual(self.g3.get_sqr(1, 2), [2, 7, 0, 0, 1, 5, 8, 6, 9])
        self.assertEqual(self.g3.get_sqr(4, 5), [6, 7, 8, 1, 3, 4, 2, 5, 9])

if __name__ == "__main__":
    unittest.main()