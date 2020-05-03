class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_array = [0]*256
        for item in magazine:
            char_array[ord(item)] += 1
        for item in ransomNote:
            if char_array[ord(item)] > 0:
                char_array[ord(item)] -= 1
            else:
                return False
        return True

# stub code to test solution
def stub(ransomNote, magazine):
    sol_obj = Solution()
    return sol_obj.canConstruct(ransomNote, magazine)
    
