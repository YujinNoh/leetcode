class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = []
        i, j = 0, 0
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] <= nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums2[j])
                j += 1
        

        if i != len(nums1) :
            for k in range(i, len(nums1)):
                new_list.append(nums1[k])
        elif j != len(nums2):
            for k in range(j, len(nums2)):
                new_list.append(nums2[k])
        
        return new_list[len(new_list) // 2] if len(new_list) % 2 == 1 else (new_list[(len(new_list) // 2) - 1] + new_list[len(new_list) // 2]) / 2
