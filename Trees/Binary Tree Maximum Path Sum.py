# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maximumpathsum=-float('infinity')
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def maxPathSumRecursive(root):
            if(root==None):
                return 0
            
            left=maxPathSumRecursive(root.left)
            right=maxPathSumRecursive(root.right)

            left=max(left,0)
            right=max(right,0)

            self.maximumpathsum=max(self.maximumpathsum,root.val+left+right)
            return root.val+max(left,right)

        maxPathSumRecursive(root)
        return self.maximumpathsum
        