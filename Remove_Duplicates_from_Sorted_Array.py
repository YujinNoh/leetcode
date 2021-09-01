class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2 = sorted(list(set(nums)))
        for i, val in enumerate(nums2):
            nums[i] = val
        return len(nums2)
