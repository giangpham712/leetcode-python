import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [4, 1, 2],
            [1,3,4,2],
            [-1,3,-1]
        ],
        [
            [2,4],
            [1,2,3,4],
            [3,-1]
        ]
    )
    def test_solve(self, value):
        nums1, nums2, expected = value
        solution = Solution()
        actual = solution.solve(nums1, nums2)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
