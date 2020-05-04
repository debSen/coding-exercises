https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_idx = 0
        while True:
            if curr_idx < len(nums) - 1 and nums[curr_idx] == nums[curr_idx +1]:
                for i in range(curr_idx+1, len(nums)):
                    nums[i-1] = nums[i]
                nums.pop()
            elif curr_idx < len(nums) - 1 and nums[curr_idx] != nums[curr_idx +1]:
                curr_idx += 1
            elif curr_idx >= len(nums)- 1:
                break
            # print(curr_idx, len(nums))
        return(len(nums))
