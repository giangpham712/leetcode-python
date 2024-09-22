from typing import List

class Solution:
    def solve(self, nums: List[int], k: int) -> int:

        prefixSums = [0]

        sum = 0
        for num in nums:
            sum += num
            prefixSums.append(sum)

        total = 0

        for i in range(len(nums) + 1):
            for j in range(i + 1, len(nums) + 1):
                if prefixSums[j] - prefixSums[i] == k:
                    total += 1

        return total