import unittest
from ddt import ddt, data
from solution import TwoSum

@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [2, 7, 11, 15], 9, [0, 1]
        ],
        [
            [3, 2, 4], 6, [1, 2]
        ],
        [
            [3, 3], 6, [0, 1]
        ]
    )
    def test_solve(self, value):
        nums, target, expected = value
        solution = TwoSum()
        actual = solution.solve(nums, target)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
