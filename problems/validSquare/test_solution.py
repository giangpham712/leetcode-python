import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
[
            [0, 0], [1, 1], [1, 0], [0, 1], True
        ],
        [
            [0, 0], [1, 1], [1, 0], [0, 12], False
        ],
        [
            [1, 0], [-1, 0], [0, 1], [0, -1], True
        ],
        [
            [1, 1], [5, 3], [3, 5], [7, 7], False
        ],
        [
            [0, 0], [1, 1], [0, 0], [1, 1], False
        ]
    )
    def test_solve(self, value):
        p1, p2, p3, p4, expected = value
        solution = Solution()
        actual = solution.solve(p1, p2, p3, p4)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
