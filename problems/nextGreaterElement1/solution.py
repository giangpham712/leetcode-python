from typing import List


class Solution:
    def solve(self, nums1: List[int], nums2: List[int]) -> List[int]:

        numMap = {}

        # Use a map to track the indexes of numbers in the result list
        for i in range(len(nums1)):
            numMap[nums1[i]] = i

        # Use a monotonic decreasing stack
        stack = []
        cursor = -1

        result = [-1] * len(nums1)

        # Iterate the second list
        for i in range(len(nums2)):

            # while the current number is greater than the number on top of the stack
            # we pop the number of top of the stack and
            # set the current number as the next greater element for the popped number

            while cursor >= 0 and stack[cursor] < nums2[i]:
                popped = stack.pop()
                cursor -= 1
                if popped in numMap:
                    result[numMap[popped]] = nums2[i]

            # add the current number to the stack, the ordering of the monotonic stack
            # is maintained
            stack.append(nums2[i])
            cursor += 1

        return result
