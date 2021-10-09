class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        from bisect import bisect_left, bisect_right
        
        if target not in nums:
            return [-1, -1]
        else:
            return[bisect_left(nums, target), bisect_right(nums, target)-1]
            
