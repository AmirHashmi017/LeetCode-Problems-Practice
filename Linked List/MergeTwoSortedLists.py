#Merge two sorted lists with iterative approach
def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    output=list1
    if(list1==None and list2==None):
        return None
    elif(list2==None):
        output=list1
        list1=list1.next
    elif(list1==None):
        output=list2
        list2=list2.next
    elif(list1.val<=list2.val):
        output=list1
        list1=list1.next
    else:
        output=list2
        list2=list2.next
    head=output
    
    while(list1!=None and list2!=None):
        if(list1.val<=list2.val):
            output.next=list1
            list1=list1.next
        else:
            output.next=list2
            list2=list2.next
        output=output.next
    
    if(list1!=None):
        output.next=list1
    if(list2!=None):
        output.next=list2
    
    return head

#Merge two sorted lists with Recursive approach
