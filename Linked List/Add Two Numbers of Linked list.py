def addTwoNumbers(l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        current=dummy
        carry=0
        while(l1 or l2 or carry):
            num1=l1.val if l1 else 0
            num2=l2.val if l2 else 0
            outputnum=num1+num2+carry
            carry=outputnum//10
            outputnum=outputnum%10
            
            current.next=ListNode(outputnum)
            current=current.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next