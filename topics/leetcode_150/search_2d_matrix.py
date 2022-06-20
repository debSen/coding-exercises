class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for idx, item in enumerate(matrix):
            if item[-1]>= target:
                target_row = idx
                break
        else:
            return False
        
        low = 0
        high = len(matrix[0]) - 1
        
        while low <= high:
            mid = int(low + (high - low)/2)
            if matrix[idx][mid] == target:
                return True
            elif matrix[idx][mid] > target:
                high -= 1
            else:
                low += 1
            print(mid)
        return False