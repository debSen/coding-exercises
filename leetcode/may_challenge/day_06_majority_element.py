class Solution:
    def majorityElement(self, nums):
        count_dict = {}
        nums_len = len(nums)
        for idx in range(int(nums_len/2)):
            if nums[idx] in count_dict:
                count_dict[nums[idx]] += 1
            else:
                count_dict[nums[idx]] = 1
        for idx in range(int(nums_len/2), nums_len):
            if nums[idx] in count_dict:
                count_dict[nums[idx]] += 1
            else:
                count_dict[nums[idx]] = 1
            if count_dict[nums[idx]] >= nums_len/2:
                return nums[idx]

# stub code
def stub(nums):
    sol_obj = Solution()
    return sol_obj.majorityElement(nums)
