class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = int(low + (high - low)/2)
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                    low = mid+1
            else:
                high -= 1
        return -1