class Solution:
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        for idx,num in enumerate(nums[:-2]):
            if idx%2 == 0 and num != nums[idx+1]:
                return num
        return nums[-1]

#Test Code
def stub(nums):
    sol_obj = Solution()
    return sol_obj.singleNonDuplicate(nums)
