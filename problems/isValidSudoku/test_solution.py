import unittest
from ddt import ddt, data
from solution import IsValidSudoku

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
            True
        ],
        [
            [["8", "3", ".", ".", "7", ".", ".", ".", "."]
                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
            False
        ]
    )
    def test_solve(self, value):
        board, expected = value
        solution = IsValidSudoku()
        actual = solution.solve(board)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
