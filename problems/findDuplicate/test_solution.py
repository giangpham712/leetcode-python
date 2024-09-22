import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [1, 3, 4, 2, 2], 2
        ],
        [
            [3, 1, 3, 4, 2], 3
        ],
        [
            [3, 3, 3, 3, 3], 3
        ]
    )
    def test_solve(self, value):
        nums, expected = value
        solution = Solution()
        actual = solution.solve(nums)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
