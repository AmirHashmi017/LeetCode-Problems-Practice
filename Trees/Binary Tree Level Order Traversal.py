# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result=[]
        level=0
        elements=1
        queue=[root]
        while queue:
            levelres=[]
            count=0
            for i in range(0,elements,1):
                node=queue.pop(0)
                levelres.append(node.val)
                if node.left:
                    queue.append(node.left)
                    count+=1
                if node.right:
                    queue.append(node.right)
                    count+=1
            result.append(levelres)
            elements=count
            
        return result
            

        