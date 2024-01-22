from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        cursor1 = m - 1
        cursor2 = n - 1
        count = 0

        while cursor2 >= 0:
            if cursor1 < 0 or nums1[cursor1] < nums2[cursor2]:
                nums1[m + n - count - 1] = nums2[cursor2]
                cursor2 = cursor2 - 1
            else:
                nums1[m + n - count - 1] = nums1[cursor1]
                cursor1 = cursor1 - 1

            count = count + 1





