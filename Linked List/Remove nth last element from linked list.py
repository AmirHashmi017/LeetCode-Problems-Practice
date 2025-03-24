def removeNthFromEnd(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    totallength=0
    if head==None or head.next==None:
        return None
    current=head
    while current!=None:
        totallength+=1
        current=current.next
    targetindex=totallength-n
    if(targetindex==0):
        head=head.next
        return head
    current=head
    for i in range(0,targetindex-1,1):
        current=current.next
    current.next=current.next.next
    return head