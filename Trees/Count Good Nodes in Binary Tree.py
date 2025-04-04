# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.goodnodes=0

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maximum=root.val
        self.goodnodesrecursive(root,maximum)
        return self.goodnodes
    
    def goodnodesrecursive(self,node,maximum):
        if not node:
            return None
        
        if node.val>=maximum:
            self.goodnodes+=1

        maximum=max(maximum,node.val)
        self.goodnodesrecursive(node.left,maximum)
        self.goodnodesrecursive(node.right,maximum)