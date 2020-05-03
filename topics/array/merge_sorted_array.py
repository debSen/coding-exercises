class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx_nums1 = 0
        idx_nums2 = 0
        
        for idx in range(len(nums1)):
            if idx_nums2 < len(nums2) and (nums1[idx_nums1] > nums2[idx_nums2]):
                for i in range(len(nums1)-2, idx_nums1-1, -1):
                    nums1[i + 1] = nums1[i]
                nums1[idx_nums1] = nums2[idx_nums2]    
                idx_nums2 += 1
                idx_nums1 += 1
            elif idx_nums2 < len(nums2) and nums1[idx_nums1] <= nums2[idx_nums2]:
                idx_nums1 += 1
                
