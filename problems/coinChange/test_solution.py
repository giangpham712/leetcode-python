import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [1, 2, 5], 11, 3
        ],
        [
            [2], 3, -1
        ],
        [
            [1], 0, 0
        ]
    )
    def test_solve(self, value):
        coins, amount, expected = value
        solution = Solution()
        actual = solution.solve(coins, amount)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
