class Solution:
    def reverse(self, x: int) -> int:
        reverse = str(x)[::-1]
        answer = int(reverse) if x >= 0 else int(reverse[0:-1]) * -1
        return 0 if answer > 2**31 or answer < 2**31*-1 else answer