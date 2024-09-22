from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:

        minProduct = nums[0]
        maxProduct = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxProduct, minProduct = minProduct, maxProduct

            maxProduct = max(maxProduct * nums[i], nums[i])
            minProduct = min(minProduct * nums[i], nums[i])
            result = max(result, maxProduct)

        return result