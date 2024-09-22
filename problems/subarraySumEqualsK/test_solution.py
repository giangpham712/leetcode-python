import unittest
from ddt import ddt, data
from solution import Solution
from solution2 import Solution2

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [1, 1, 1],
            2,
            2
        ],
        [
            [1, 2, 3],
            3,
            2
        ],
        [
            [1, 2, 1, 2, 1],
            3,
            4
        ]
    )
    def test_solve(self, value):
        nums, k, expected = value
        solution = Solution()
        actual = solution.solve(nums, k)
        self.assertEqual(expected, actual)  # add assertion here

    @data(
        [
            [1, 1, 1],
            2,
            2
        ],
        [
            [1, 2, 3],
            3,
            2
        ],
        [
            [1, 2, 1, 2, 1],
            3,
            4
        ]
    )
    def test_solve2(self, value):
        nums, k, expected = value
        solution = Solution2()
        actual = solution.solve(nums, k)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
