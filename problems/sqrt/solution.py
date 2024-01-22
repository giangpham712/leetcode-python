from unittest import result


class Solution:
    def sqrt(self, x: int) -> int:
        if x == 0:
            return 0

        if x == 1:
            return 1

        start = 0
        end = x

        while True:
            mid = (start + end) // 2
            if mid == start:
                return mid

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid
            else:
                start = mid



