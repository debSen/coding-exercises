from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = Counter(s)
        for idx, item in enumerate(s):
            if count_dict[item] == 1:
                return idx
        return -1

# Test Code
def stub(s):
    sol_obj = Solution()
    return sol_obj.firstUniqChar(s)
