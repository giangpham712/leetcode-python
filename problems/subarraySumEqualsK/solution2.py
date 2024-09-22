from typing import List

# We have to find the total number of sub-arrays whose total element sum is equal to a given integer k The idea is to
# keep on taking cumulative sum of the array and count these cumulative sum values by using an unordered map. If the
# sum becomes k, that means all elements up till here make a valid subarray and so we increment our result by one.
#
# Otherwise, if our current cumulative sum is not equal to k, that means somewhere in the array, we need value
# current cumulative sum - k. Since we store cumulative sum at every step in a map, we could check in the map if we
# had encountered this value. If yes, that means a valid sub array is possible. Hence we increment our result by the
# frequency of this value in the map.

class Solution2:
    def solve(self, nums: List[int], k: int) -> int:

        total = 0
        sumFrequency: map[int:int] = { 0: 1 }
        sum = 0

        for num in nums:
            sum += num

            if sum - k in sumFrequency:
                total += sumFrequency[sum - k]

            if sum in sumFrequency:
                sumFrequency[sum] += 1
            else:
                sumFrequency[sum] = 1

        return total