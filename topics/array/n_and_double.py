# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        item_array = []
        for item in arr:
            if item/2 in item_array or item*2 in item_array:
                return True
            else:
                item_array.append(item)
        return False
