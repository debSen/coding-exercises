class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:
            return False
        

        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        