import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [[1, 4, 5], [1, 3, 4], [2, 6]],
            [1, 1, 2, 3, 4, 4, 5, 6]
        ],
        [
            [],
            []
        ],
        [
            [[]],
            []
        ]
    )
    def test_solve(self, value):
        expected = value
        solution = Solution()
        actual = solution.solve()
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
