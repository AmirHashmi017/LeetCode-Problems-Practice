# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        queue=[[root,float('-infinity'),float('infinity')]]
        while queue:
            node,left,right=queue.pop(0)
            if not(left<node.val<right):
                return False
            if node.left:
                queue.append([node.left,left,node.val])
            if node.right:
                queue.append([node.right,node.val,right])
        
        return True
    
    
        

        
        
        
