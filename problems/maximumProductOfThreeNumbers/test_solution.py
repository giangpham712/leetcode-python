import unittest
from ddt import ddt, data
from solution import Solution
from solution2 import Solution2

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [1, 2, 3],
            6
        ],
        [
            [1, 2, 3, 4],
            24
        ],
        [
            [-1, -2, -3],
            -6
        ],
        [
            [-100, -98, -1, 2, 3, 4],
            39200
        ]
    )
    def test_solve(self, value):
        nums, expected = value
        solution = Solution()
        actual = solution.solve(nums)
        self.assertEqual(expected, actual)

    @data(
        [
            [1, 2, 3],
            6
        ],
        [
            [1, 2, 3, 4],
            24
        ],
        [
            [-1, -2, -3],
            -6
        ],
        [
            [-100, -98, -1, 2, 3, 4],
            39200
        ]
    )
    def test_solve(self, value):
        nums, expected = value
        solution = Solution2()
        actual = solution.solve(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
