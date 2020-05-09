class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.recurse_string(s, level=0)
    def recurse_string(self, s, level):
        if level == len(s)//2:
            return
        else:
            temp = s[level]
            s[level] = s[-(level+1)]
            s[-(level+1)] = temp
            self.recurse_string(s, level+1)
