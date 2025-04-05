# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.hashmapinorder={}
        self.idx=0
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        for i in range(len(inorder)):
            self.hashmapinorder[inorder[i]]=i
        
        def DFSRecursive(left,right):
            if(left>right):
                return None

            rootval=preorder[self.idx]
            self.idx+=1

            root=TreeNode(rootval)
            mid=self.hashmapinorder[rootval]
            

            root.left=DFSRecursive(left,mid-1)
            root.right=DFSRecursive(mid+1,right)
            return root
        
        return DFSRecursive(0,len(inorder)-1)
    
    

        

        
        


            
        