# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sortedtree=[]
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.treeInorder(root)
        return self.sortedtree[k-1]
    
    def treeInorder(self,root):
        if not root:
            return None
        self.treeInorder(root.left)
        self.sortedtree.append(root.val)
        self.treeInorder(root.right)
        

        