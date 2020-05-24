from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(ch*count for count,ch in Counter(s).most_common())
            
