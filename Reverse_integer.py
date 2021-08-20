class Solution:
    def reverse(self, x: int) -> int:
        answer = int(str(x)[::-1]) if x >= 0 else -1 * int(str(-1 * x)[::-1])
        if answer <= (2**31 - 1) and answer >= -2**31:
            return answer
        else:
            return 0
