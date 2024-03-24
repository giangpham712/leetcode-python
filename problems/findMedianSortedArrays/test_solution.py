import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [1, 3], [2], 2.0
        ],
        [
            [1, 2], [3, 4], 2.5
        ]
    )
    def test_solve(self, value):
        nums1, nums2, expected = value
        solution = Solution()
        actual = solution.solve(nums1, nums2)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
