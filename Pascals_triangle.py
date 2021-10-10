class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        array = [1] * 30
        array[0] = [1]
        array[1] = [1,1]
        
        for i in range(2,30):
            array[i] = [1]
            for k in range(i-1):
                array[i].append(array[i - 1][k] + array[i - 1][k + 1])
            array[i].append(1)
        
        return array[0:numRows]
