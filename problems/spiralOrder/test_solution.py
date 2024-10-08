import unittest
from ddt import ddt, data
from solution import Solution

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1,2,3,6,9,8,7,4,5]
        ],
        [
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1,2,3,4,8,12,11,10,9,5,6,7]
        ]
    )
    def test_solve(self, value):
        matrix, expected = value
        solution = Solution()
        actual = solution.solve(matrix)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
