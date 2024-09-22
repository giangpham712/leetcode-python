import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            "1432219",
            3,
            "1219"
        ],
        [
            "10200",
            1,
            "200"
        ],
        [
            "10",
            2,
            "0"
        ]
    )
    def test_solve(self, value):
        num, k, expected = value
        solution = Solution()
        actual = solution.solve(num, k)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
