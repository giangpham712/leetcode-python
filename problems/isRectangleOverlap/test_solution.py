import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [0, 0, 2, 2],
            [1, 1, 3, 3],
            True
        ],
        [
            [0, 0, 1, 1],
            [1, 0, 2, 1],
            False
        ],
        [
            [0, 0, 1, 1],
            [2, 2, 3, 3],
            False
        ]
    )
    def test_solve(self, value):
        rec1, rec2, expected = value
        solution = Solution()
        actual = solution.solve(rec1, rec2)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
