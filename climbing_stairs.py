class Solution:
    def climbStairs(self, n: int) -> int:
        array = [0] * 46
        array[1] = 1
        array[2] = 2
        
        for i in range(3, 46):
            array[i] = array[i - 1] + array[i - 2]
        
        return array[n]
