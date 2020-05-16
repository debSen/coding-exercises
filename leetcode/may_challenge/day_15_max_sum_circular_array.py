class Solution:
    def maxSubarraySumCircular(self, A):
        if len(A) == 0:
            return 0
        max_total = A[0]
        max_so_far = A[0]
        min_so_far = A[0]
        min_total = A[0]
        s = A[0]
        for i in range(1, len(A)):
            max_so_far = max(A[i], max_so_far + A[i])
            max_total = max(max_total, max_so_far)            
            
            min_so_far = min(A[i], min_so_far + A[i])            
            min_total = min(min_total, min_so_far)            
            s += A[i]
        if(s == min_total):
            return max_total
        
        return max(s - min_total, max_total)

# Test Code
def stub(A):
    sol_obj = Solution()
    return sol_obj.maxSubarraySumCircular(A)
