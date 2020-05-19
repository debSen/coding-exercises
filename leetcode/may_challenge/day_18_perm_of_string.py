from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_len = len(s2)
        s1_len = len(s1)
        s1_dict = Counter(s1)
        for index in range(s2_len - s1_len + 1):
            s_str = s2[index:index+s1_len]
            if Counter(s_str) == s1_dict:
                return True
        return False

def stub(s1, s2):
    sol_obj = Solution()
    return sol_obj.checkInclusion(s1, s2)
