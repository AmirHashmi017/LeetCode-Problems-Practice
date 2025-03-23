def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slowptr=head
    fastptr=head
    while(fastptr!=None and fastptr.next!=None):
        slowptr=slowptr.next
        fastptr=fastptr.next.next
        if(slowptr==fastptr):
            return True
    
    return False