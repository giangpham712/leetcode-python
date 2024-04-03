import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            "egg", "add", True
        ],
        [
            "foo", "bar", False
        ],
        [
            "paper", "title", True
        ]
    )
    def test_solve(self, value):
        s, t, expected = value
        solution = Solution()
        actual = solution.solve(s, t)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
