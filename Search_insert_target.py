# version 1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)
          
# version 2
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i, val in enumerate(nums):
                if target < val:
                    return i
                elif target > max(nums):
                    return len(nums)
