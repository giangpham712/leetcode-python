import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
             "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"],
            ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"]
        ],
        [
            ["a/*comment", "line", "more_comment*/b"],
            ["ab"]
        ],
        [
            ["main() {", "   int x = 1; // Its comments here", "   x++;", "   cout << x;", "   //return x;", "   x--;",
             "}"],
            ["main() {", "   int x = 1; ", "   x++;", "   cout << x;", "   ", "   x--;", "}"]
        ]
    )
    def test_solve(self, value):
        source, expected = value
        solution = Solution()
        actual = solution.solve(source)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
