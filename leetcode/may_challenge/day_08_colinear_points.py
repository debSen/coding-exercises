class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) <= 2:
            return True
        else:
            #Check colinearity of thrid point onward with first two points
            for idx in range(2,len(coordinates)):
                if not self.check_colinear(coordinates[0], coordinates[1], coordinates[idx]):
                    return False
            return True
    
    def check_colinear(self, p1, p2, p3):
        # Calculate area of triangle
        # if area is zero then straight line
        area = p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]) 
  
        if area != 0:
            return False
        else:
            return True

def stub(coords):
    sol_obj = Solution()
    return sol_obj.checkStraightLine(coords)
