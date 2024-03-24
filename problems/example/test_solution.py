import unittest
from ddt import ddt, data
from solution import Solution


class SolutionTestCase(unittest.TestCase):

    @data(
        [
        ]
    )
    def test_solve(self, value):
        expected = value
        solution = Solution()
        actual = solution.solve()
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
