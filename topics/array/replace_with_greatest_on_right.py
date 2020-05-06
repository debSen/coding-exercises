# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/


class Solution:
    def replaceElements(self, arr):
        for idx, item in enumerate(arr[:-1]):
            arr[idx] = max(arr[idx+1:])
        arr[-1] = -1
        return arr

def stub(arr):
    sol_obj = Solution()
    return sol_obj.replaceElements(arr)
