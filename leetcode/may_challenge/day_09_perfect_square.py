# Babylonian Method
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return True
        x = num // 2
        seen = set([x])
        while x * x != num:
            x = (x + (num // x)) // 2
            if x in seen: 
                return False
            seen.add(x)
        return True

# test code
def stub(num):
    sol_obj = Solution()
    return sol_obj.isPerfectSquare(num)
