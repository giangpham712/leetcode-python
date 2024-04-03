class Solution:
    def solve(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mappings1 = {}
        mappings2 = {}

        for i in range(len(s)):
            if s[i] not in mappings1:
                mappings1[s[i]] = t[i]
            elif mappings1[s[i]] != t[i]:
                return False

            if t[i] not in mappings2:
                mappings2[t[i]] = s[i]
            elif mappings2[t[i]] != s[i]:
                return False

        return True
