import unittest
from ddt import ddt, data
from solution import Solution, Node


@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        [
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        ],
        [
            [[3, None], [3, 0], [3, None]],
            [[3, None], [3, 0], [3, None]]
        ]
    )
    def test_solve(self, value):
        input, expected = value
        solution = Solution()

        currentNode = None
        nodes = []
        for [val, random] in input:
            prevNode = currentNode
            currentNode = Node(val)
            if prevNode is not None:
                prevNode.next = currentNode

            nodes.append(currentNode)

        for idx, [val, random] in enumerate(input):
            if random is not None:
                nodes[idx].random = nodes[random]

        copy = solution.solve(nodes[0])

        actual = []

        map = {}
        currentCopy = copy
        idx = 0
        while currentCopy is not None:
            actual.append([currentCopy.val, None])
            map[currentCopy] = idx
            currentCopy = currentCopy.next
            idx = idx + 1

        currentCopy = copy
        idx = 0
        while currentCopy is not None:
            if currentCopy.random is not None:
                actual[idx][1] = map[currentCopy.random]
            currentCopy = currentCopy.next
            idx = idx + 1

        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
