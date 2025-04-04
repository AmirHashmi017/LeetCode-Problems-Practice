# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        rightsideview=[]
        queue=[root]
        element=1
        while queue:
            count=0
            for i in range(0,element,1):
                node=queue.pop(0)
                if(i==element-1):
                    rightsideview.append(node.val)
                if node.left:
                    queue.append(node.left)
                    count+=1
                if node.right:
                    queue.append(node.right)
                    count+=1
            element=count
        
        return rightsideview