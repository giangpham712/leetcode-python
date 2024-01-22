import unittest
import itertools
from ddt import ddt, data

from problems.mergeSortedArrays.solution import Solution


@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]],
        [[1], 1, [], 0, [1]],
        [[0], 0, [1], 1, [1]],
        [[2, 0], 1, [1], 1, [1, 2]],
    )
    def test_merge(self, value):
        nums1, m, nums2, n, expected = value
        solution = Solution()
        solution.merge(nums1, m, nums2, n)
        self.assertListEqual(expected, nums1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
