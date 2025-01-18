class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if(not self.minstack):
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1],val))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minstack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

        
obj = MinStack()
obj.push(-3)
obj.push(0)
obj.push(-2)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
print(obj.minstack)