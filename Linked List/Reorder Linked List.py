def reorderList(head):
    """
    :type head: Optional[ListNode]
    :rtype: None Do not return anything, modify head in-place instead.
    """
    slowptr=head
    fastptr=head.next
    while(fastptr!=None and fastptr.next!=None):
        slowptr=slowptr.next
        fastptr=fastptr.next.next
    reversehead=slowptr
    
    prev=None
    nextptr=None
    while reversehead!=None:
        nextptr=reversehead.next
        reversehead.next=prev
        prev=reversehead
        reversehead=nextptr
    
    tail=prev
    current=head
    currnext=None
    tailnext=None
    while(current!=None and tail!=None):
        currnext=current.next
        tailnext=tail.next
        current.next=tail
        tail.next=currnext
        tail=tailnext
        current=currnext