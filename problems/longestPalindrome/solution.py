class Solution:
    def solve(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        isPalindrome = [[False for x in range(n)] for y in range(n)]

        longest = s[0]

        for i in range(0, n):
            for j in range(0, i + 1):
                if s[i] == s[j]:
                    isPalindrome[j][i] = (i - j <= 2) or isPalindrome[j + 1][i - 1]
                    if isPalindrome[j][i]:
                        if len(s[j:i+1]) > len(longest):
                            longest = s[j:i+1]

        return longest
