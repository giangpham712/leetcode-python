import unittest
from solution import Solution
from ddt import ddt, data

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [[2, 3, 6, 7], 7, [[2, 2, 3], [7]]],
        [[2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]],
    )
    def test_combinationSum(self, value):
        candidates, target, expected = value
        solution = Solution()
        actual = solution.combinationSum(candidates, target)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
