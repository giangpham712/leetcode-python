from typing import List

class MissingNumber:
    def solve(self, nums: List[int]) -> int:
        n = len(nums) + 1
        return sum(range(n)) - sum(nums)
