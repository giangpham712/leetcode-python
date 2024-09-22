import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]],
            6
        ],
        [
            [["0"]],
            0
        ],
        [
            [["1"]],
            1
        ]
    )
    def test_solve(self, value):
        matrix, expected = value
        solution = Solution()
        actual = solution.solve(matrix)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
