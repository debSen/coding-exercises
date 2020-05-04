# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr_idx = 0
        for idx in range(len(nums)):
            if curr_idx < len(nums) and nums[curr_idx] == val:
                for i in range(curr_idx + 1, len(nums)):
                    nums[i-1] = nums[i]
                nums.pop()
            else:
                curr_idx += 1
        return(len(nums))
