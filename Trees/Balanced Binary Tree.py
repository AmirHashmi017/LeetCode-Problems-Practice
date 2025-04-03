# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.isbalanced=True
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.isBalancedrecursive(root)
        return self.isbalanced
        
    def isBalancedrecursive(self,root):
        if not root:
            return 0

        left=self.isBalancedrecursive(root.left)
        right=self.isBalancedrecursive(root.right)

        if abs(left-right)>1:
            self.isbalanced=False

        return 1+max(left,right)
