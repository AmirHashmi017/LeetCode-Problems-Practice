class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def inserttolist(self,node):
        #Inserting newnode between dummy pointers
        prev=self.right.prev
        nxt=self.right
        prev.next=node
        nxt.prev=node
        node.prev=prev
        node.next=nxt
    
    def removefromlist(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if(key not in self.cache):
            return -1
        self.removefromlist(self.cache[key])
        self.inserttolist(self.cache[key])
        return self.cache[key].val
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.cache:
            self.removefromlist(self.cache[key])

        self.cache[key]=Node(key,value)
        self.inserttolist(self.cache[key])

        if len(self.cache)>self.cap:
            LRU=self.left.next
            self.removefromlist(LRU)
            del(self.cache[LRU.key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)