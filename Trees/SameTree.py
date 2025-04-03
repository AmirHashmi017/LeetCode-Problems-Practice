# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
       
        queuep=[p]
        queueq=[q]

        while(queuep and queueq):
            nodep=queuep.pop(0)
            nodeq=queueq.pop(0)
            if(not nodep and not nodeq):
                continue
            elif(not nodep or not nodeq or nodep.val!=nodeq.val):
                return False
                
            queuep.append(nodep.left)
            queuep.append(nodep.right)
            queueq.append(nodeq.left)
            queueq.append(nodeq.right)

        
        if(not queuep and not queueq):
            return True
        return False
        