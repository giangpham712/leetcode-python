import unittest
from ddt import ddt, data
from solution import MissingNumber

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [3, 0, 1],
            2
        ],
        [
            [0,1],
            2
        ],
        [
            [9,6,4,2,3,5,7,0,1],
            8
        ]
    )
    def test_solve(self, value):
        nums, expected = value
        solution = MissingNumber()
        actual = solution.solve(nums)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
