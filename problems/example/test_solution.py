import unittest
from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        solution.solve()
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
