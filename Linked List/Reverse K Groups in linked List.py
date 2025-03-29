# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        groupstart=dummy

        while True:
            kth=self.FindKth(groupstart,k)
            if not kth:
                break
            groupNext=kth.next
            prev=kth.next
            current=groupstart.next
            
            while(current!=groupNext):
                tmp=current.next
                current.next=prev
                prev=current
                current=tmp
            
            tmp=groupstart.next
            groupstart.next=kth
            groupstart=tmp
        return dummy.next

        
    def FindKth(self,current,k):
        while(current and k>0):
            current=current.next
            k-=1
        return current