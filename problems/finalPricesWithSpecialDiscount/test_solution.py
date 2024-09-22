import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [8, 4, 6, 2, 3],
            [4, 2, 4, 2, 3]
        ],
        [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]
        ],
        [
            [10, 1, 1, 6],
            [9, 0, 1, 6]
        ]
    )
    def test_solve(self, value):
        prices, expected = value
        solution = Solution()
        actual = solution.solve(prices)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
