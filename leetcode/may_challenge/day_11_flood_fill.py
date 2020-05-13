class Solution:
    def floodFill(self, image, sr, sc, newColor):
        startColor = image[sr][sc]
        # visited = [[0]*len(image[0])]*len(image)
        visited = [[0 for x in range(len(image[0]))] for y in range(len(image))]
        self.recursePaint(image, sr, sc, newColor, startColor, visited)
        return image
        
    def recursePaint(self, image, sr, sc, newColor, startColor, visited):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
            return

        if image[sr][sc] == startColor and not visited[sr][sc]:
            image[sr][sc] = newColor
            visited[sr][sc] = 1
            self.recursePaint(image, sr-1, sc, newColor, startColor, visited)
            self.recursePaint(image, sr+1, sc, newColor, startColor, visited)
            self.recursePaint(image, sr, sc-1, newColor, startColor, visited)
            self.recursePaint(image, sr, sc+1, newColor, startColor, visited)

def stub(image, sr, sc, newColor):
    sol_obj = Solution()
    return sol_obj.floodFill(image, sr, sc, newColor) 
