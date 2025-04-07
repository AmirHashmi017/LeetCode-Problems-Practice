# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"
        result=[]
        queue=[root]
        while queue:
            node=queue.pop(0)
            if not node:
                result.append("N")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals=data.split(",")
        if vals[0]=="N":
            return None
        root=TreeNode(vals[0])
        queue=[root]
        i=1
        while queue:
            node=queue.pop(0)
            if(vals[i]!="N"):
                node.left=TreeNode(vals[i])
                queue.append(node.left)
            i+=1
            if(vals[i]!="N"):
                node.right=TreeNode(vals[i])
                queue.append(node.right) 
            i+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))