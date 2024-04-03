class Solution:
    def solve(self, n: int) -> bool:
        return n & (n << 1) == 0
