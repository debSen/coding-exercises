class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        result_list = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1]==B[j-1]:
                    result_list[i][j] = result_list[i-1][j-1]+1
                else:
                    result_list[i][j] = max(result_list[i-1][j], result_list[i][j-1])
        
        return result_list[m][n]
