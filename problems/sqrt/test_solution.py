import unittest
import itertools
from ddt import ddt, data

from problems.sqrt.solution import Solution


@ddt
class SolutionTestCase(unittest.TestCase):

    @data([4, 2], [8, 2])
    def test_sqrt(self, value):
        number, expected = value
        solution = Solution()
        self.assertEqual(expected, solution.sqrt(number))  # add assertion here


if __name__ == '__main__':
    unittest.main()
