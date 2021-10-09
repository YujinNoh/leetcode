class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))
        left = 0
        right = len(nums) - 1
        
        if (target > max(nums)) or (target < min(nums)):
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        elif len(nums) >= 2:
            nums.sort()
            while (left <= right):
                
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    break
                
            return (mid + pivot) % len(nums) if left <= right else -1
