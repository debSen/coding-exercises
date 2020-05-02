class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for stone in S:
            if stone in J:
                count += 1
        return count

# Solution stub code for pytest
def stub(J, S):
    sol_obj = Solution()
    return sol_obj.numJewelsInStones(J, S)
