from typing import List

class Solution:
    def solve(self, nums: List[int]) -> int:

        b = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in b:
                return i

        return len(nums) + 1
