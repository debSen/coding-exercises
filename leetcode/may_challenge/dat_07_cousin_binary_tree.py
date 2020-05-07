class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if self.check_sibling(root,x,y):
            return False
        x_depth = self.check_depth(root, x, depth)
        y_depth = self.check_depth(root, y, depth)
        if x_depth == y_depth:
            return True
        
    def check_depth(self, node, x, depth):
        if (node == None): 
            return 0

        if (node.val == x) : 
            return depth  

        downlevel = self.check_depth(node.left, 
                                 x, depth + 1)  
        if (downlevel != 0) : 
            return downlevel  

        downlevel = self.check_depth(node.right,  
                                 x, depth + 1)  
        return downlevel  

    def check_sibling(self, node, x, y):
        if node is None:
            return False
        if node.left and node.right:
            if node.left.val == x and node.right.val == y:
                return True
            elif node.left.val == y and node.right.val == x:
                return True
        if node.left is not None:
            if self.check_sibling(node.left, x, y):
                return True
        if node.right is not None:
            if self.check_sibling(node.right, x, y):
                return True
    
            
