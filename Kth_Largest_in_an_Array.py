class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        
        h = []
        
        for val in nums:
            heapq.heappush(h, -val)
        
        for i in range(k):
            answer = heapq.heappop(h)
        
        return -answer
