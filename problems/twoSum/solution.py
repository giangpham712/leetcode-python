from typing import List

class TwoSum:
    def solve(self, nums: List[int], target: int) -> List[int]:
        missings = dict()
        for idx, a in enumerate(nums):
            if a in missings:
                return [missings[a], idx]

            missings[target - a] = idx
