class Solution:
    def solve(self, num: str, k: int) -> str:
        stack = []

        cursor = -1
        for digit in num:
            while k > 0 and cursor >= 0 and stack[cursor] > digit:
                stack.pop()
                cursor -= 1
                k = k - 1

            stack.append(digit)
            cursor += 1

        result = ''.join(stack)[0:(len(stack) - k)]

        result = result.lstrip('0')

        if result == '':
            return '0'

        return result
