import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [2, 1, 5, 6, 2, 3],
            10
        ],
        [
            [2, 4],
            4
        ]
    )
    def test_solve(self, value):
        heights, expected = value
        solution = Solution()
        actual = solution.solve(heights)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
