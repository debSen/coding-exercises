class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        for i in range(k):
            j = 0
            while (j < len(num) - 1) and ord(num[j]) <= ord(num[j + 1]):
                j+= 1
            num = num[:j] + num[j+1:]
        num = num.lstrip("0")
        if num:
            return num
        else:
            return "0"

def stub(num, k):
    sol_obj = Solution()
    return sol_obj.removeKdigits(num, k)
