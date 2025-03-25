def copyRandomList(head):
    """
    :type head: Node
    :rtype: Node
    """
    hashmap={None:None}
    current=head
    while current!=None:
        copy=Node(current.val)
        hashmap[current]=copy
        current=current.next
    
    current=head
    while current!=None:
        copy=hashmap[current]
        copy.next=hashmap[current.next]
        copy.random=hashmap[current.random]
        current=current.next
    return hashmap[head]