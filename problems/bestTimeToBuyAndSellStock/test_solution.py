import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [7, 1, 5, 3, 6, 4],
            5
        ],
        [
            [7, 6, 4, 3, 1],
            0
        ]
    )
    def test_solve(self, value):
        prices, expected = value
        solution = Solution()
        actual = solution.solve(prices)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
