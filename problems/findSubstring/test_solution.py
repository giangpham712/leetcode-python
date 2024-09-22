import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            "barfoothefoobarman",
            ["foo", "bar"],
            [0, 9]
        ],
        [
            "wordgoodgoodgoodbestword",
            ["word", "good", "best", "word"],
            []
        ],
        [
            "barfoofoobarthefoobarman",
            ["bar", "foo", "the"],
            [6, 9, 12]
        ]
    )
    def test_solve(self, value):
        s, words, expected = value
        solution = Solution()
        actual = solution.solve(s, words)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
