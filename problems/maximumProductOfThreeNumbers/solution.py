from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        nums.sort()

        if nums[0] * nums[1] * nums[len(nums) - 1] > nums[len(nums) - 3] * nums[len(nums) - 2] * nums[len(nums) - 1]:
            return nums[0] * nums[1] * nums[len(nums) - 1]
        else:
            return nums[len(nums) - 3] * nums[len(nums) - 2] * nums[len(nums) - 1]

