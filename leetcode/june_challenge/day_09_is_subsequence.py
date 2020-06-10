class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0 and len(s) != 0:
            return False
        current_s = 0
        for item in t:
            # print(item)
            if item == s[current_s]:
                # print(s[current_s])
                current_s += 1
            if current_s == len(s):

                return True
        return False
