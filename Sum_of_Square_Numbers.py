class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        else:
            for i in range(c):
                squareB = c - i*i
                if squareB < 0:
                    return False
                elif squareB ** 0.5 == round(squareB ** 0.5):
                    return True
                    break
            return False
