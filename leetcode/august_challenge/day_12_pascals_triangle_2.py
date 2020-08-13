class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        
        for i in range(1, rowIndex+1):
            lastrow = row
            row = []
            row = [1]
            for j in range(1, i):
                row.append(lastrow[j-1] + lastrow[j])
            row.append(1)
        
        return row
