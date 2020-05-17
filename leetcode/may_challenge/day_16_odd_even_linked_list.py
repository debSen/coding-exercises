class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:  
            return None
 
        odd = head  
        even = head.next
  
        evenFirst = even  
  
        while True:  
            if odd == None or even == None or even.next == None:  
                odd.next = evenFirst  
                break
  
            odd.next = even.next
            odd = even.next

            if odd.next == None:  
                even.next = None
                odd.next = evenFirst  
                break

            even.next = odd.next
            even = odd.next
        return head
