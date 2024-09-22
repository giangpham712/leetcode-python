import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [2, 3, -2, 4],
            6
        ],
        [
            [-2, 0, -1],
            0
        ]
    )
    def test_solve(self, value):
        nums, expected = value
        solution = Solution()
        actual = solution.solve(nums)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
