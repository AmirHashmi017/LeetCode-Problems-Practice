# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        queue=[root]
        while queue:
            node=queue.pop(0)
            if(self.isSameTree(node,subRoot)):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def isSameTree(self, p, q):
        
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
        