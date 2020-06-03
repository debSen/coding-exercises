class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_d = {}
        count_d[0] = -1
        max_len= 0
        count = 0
        for idx, item in enumerate(nums):
            if not item:
                count += -1
            else:
                count+= 1
            if count in count_d:
                max_len = max(max_len, idx - count_d[count])
            else:
                count_d[count] = idx
        return max_len
