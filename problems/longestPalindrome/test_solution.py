import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            "babad",
            ["bab", "aba"]
        ],
        [
            "cbbd",
            ["bb"]
        ],
        [
            "ac",
            ["a", "c"]
        ],
        [
            "aaaa",
            ["aaaa"]
        ]
    )
    def test_solve(self, value):
        s, expected = value
        solution = Solution()
        actual = solution.solve(s)
        self.assertIn(actual, expected)


if __name__ == '__main__':
    unittest.main()
