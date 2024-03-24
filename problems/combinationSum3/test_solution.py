import unittest
from solution import Solution
from ddt import ddt, data

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            3,
            7,
            [
                [1,2,4]
            ]
        ],
        [
            3,
            9,
            [
                [1,2,6],[1,3,5],[2,3,4]
            ]
        ],
        [
            4,
            1,
            []
        ]
    )
    def test_combinationSum3(self, value):
        k, n, expected = value
        solution = Solution()
        actual = solution.combinationSum3(k, n)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
