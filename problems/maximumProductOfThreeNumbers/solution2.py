from typing import List


class Solution2:
    def solve(self, nums: List[int]) -> int:
        min1 = 1000
        min2 = 1000
        max1 = -1000
        max2 = -1000
        max3 = -1000

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num


        return max(min1 * min2 * max1, max3 * max2 * max1)

