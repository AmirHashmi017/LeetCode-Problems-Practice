def reverseList(head):
    current=head
    prevp=None
    nextp=None
    while(current!=None):
        nextp=current.next
        current.next=prevp
        prevp=current
        current=nextp
    
    head=prevp
    return head

# print(reverseList([1,2,3,4,5]))