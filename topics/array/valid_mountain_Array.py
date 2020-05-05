# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/


class Solution:
    def validMountainArray(self, A):
        valley_started = False
        mount_started = False
        if len(A) <= 2:
            return False
        for idx in range(len(A)-1):
            if A[idx+1] == A[idx]:
                return False
            if A[idx+1] < A[idx] and not valley_started:
                valley_started = True
            if A[idx+1] > A[idx] and valley_started:
                return False
            if A[idx+1] > A[idx] and not mount_started:
                mount_started = True
        if not (valley_started and mount_started):
            return False
        return True

def stub(A):
    sol_obj = Solution()
    return sol_obj.validMountainArray(A)
