# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if(not lists or len(lists)==0):
            return None
        while(len(lists)>1):
            mergedlists=[]
            for i in range(0,len(lists),2):
                list1=lists[i]
                list2=lists[i+1] if (i+1)<len(lists) else None
                mergedlists.append(self.mergeLists(list1,list2))
            lists=mergedlists
        return lists[0]
    
    def mergeLists(self,list1,list2):

        sortedlist=ListNode()
        head=sortedlist
        while(list1!=None and list2!=None):
            if(list1.val<=list2.val):
                sortedlist.next=list1
                list1=list1.next
            else:
                sortedlist.next=list2
                list2=list2.next
            sortedlist=sortedlist.next
        
        if(list1!=None):
            sortedlist.next=list1
            sortedlist=sortedlist.next
        
        if(list2!=None):
            sortedlist.next=list2
            sortedlist=sortedlist.next
        
        return head.next
        
            

        