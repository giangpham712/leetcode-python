import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [1, 2, 0], 3
        ],
        [
            [3, 4, -1, 1], 2
        ],
        [
            [7, 8, 9, 11, 12], 1
        ]
    )
    def test_solve(self, value):
        nums, expected = value
        solution = Solution()
        actual = solution.solve(nums)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
