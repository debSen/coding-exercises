class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        
        while low <= high:
            mid = (high + low)//2
            # print(mid)
            if target < nums[mid] and (mid == 0 or target > nums[mid - 1]):
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid] and (mid + 1 == len(nums) or target < nums[mid + 1]):
                return mid + 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
