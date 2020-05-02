class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r =  1, n
        while l < r:
            mid = (l + r) >> 1
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


# Stub to work with pytest
def isBadVersion(version):
    return arr[version - 1]

def stub(n, version):
    global arr
    arr = [False if x < version else True for x in range(1, n+1)]
    sol_obj = Solution()
    return sol_obj.firstBadVersion(n)
