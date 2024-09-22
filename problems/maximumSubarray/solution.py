from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:

        max = nums[0]
        current = 0

        for i in range(0, len(nums)):

            if (current >= 0 and current + nums[i] < 0) or (current < 0):
                current = nums[i]
            else:
                current += nums[i]

            if current > max:
                max = current

        return max

