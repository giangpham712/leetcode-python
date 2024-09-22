from typing import List


class Solution:
    def solve(self, prices: List[int]) -> List[int]:

        cursor = -1
        stack = []

        for i in range(len(prices)):
            while cursor >= 0 and prices[i] <= prices[stack[cursor]]:
                popped = stack.pop()
                prices[popped] = prices[popped] - prices[i]
                cursor -= 1

            stack.append(i)
            cursor += 1

        return prices
