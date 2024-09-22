import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            ["i", "love", "leetcode", "i", "love", "coding"],
            2,
            ["i", "love"]
        ],
        [
            ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
            4,
            ["the", "is", "sunny", "day"]
        ],
        [
            ["i", "love", "leetcode", "i", "love", "coding"],
            1,
            ["i"]
        ]
    )
    def test_solve(self, value):
        words, k, expected = value
        solution = Solution()
        actual = solution.solve(words, k)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
