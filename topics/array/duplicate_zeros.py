class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_added = False
        for idx in range(len(arr)-1):
            if arr[idx] == 0 and not zero_added:
                for i in range(len(arr)-2,idx-1,-1):
                    arr[i+1] = arr[i]
                arr[idx+1] = 0
                zero_added = True
            elif arr[idx] == 0 and zero_added:
                zero_added = False
        return(arr)

def stub(arr):
    sol_obj = Solution()
    return sol_obj.duplicateZeros(arr)
