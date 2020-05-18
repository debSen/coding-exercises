from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        final_list = []
        s_len = len(s)
        p_len = len(p)
        p_dict = Counter(p)
        for index in range(s_len - p_len + 1):
            s_str = s[index:index+p_len]
            if Counter(s_str) == p_dict:
                final_list.append(index)
        
        return final_list

def stub(s, p):
    sol_obj = Solution()
    return sol_obj.findAnagrams(s, p)
