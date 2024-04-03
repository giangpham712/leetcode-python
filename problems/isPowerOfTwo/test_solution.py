import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            1, True
        ],
        [
            16, True
        ],
        [
            3, False
        ]
    )
    def test_solve(self, value):
        n, expected = value
        solution = Solution()
        actual = solution.solve(n)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
