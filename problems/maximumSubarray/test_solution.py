import unittest
from ddt import ddt, data
from solution import Solution
from solution2 import Solution2

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            6
        ],
        [
            [1],
            1
        ],
        [
            [5, 4, -1, 7, 8],
            23
        ],
        [
            [-1],
            -1
        ]
    )
    def test_solve(self, value):
        nums, expected = value
        solution = Solution()
        actual = solution.solve(nums)
        self.assertEqual(expected, actual)  # add assertion here

    @data(
        [
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            6
        ],
        [
            [1],
            1
        ],
        [
            [5, 4, -1, 7, 8],
            23
        ],
        [
            [-1],
            -1
        ]
    )
    def test_solve_2(self, value):
        nums, expected = value
        solution = Solution2()
        actual = solution.solve(nums)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
