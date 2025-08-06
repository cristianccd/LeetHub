# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        
        # Initialize a dummy node to build the resulting list
        dummy_head = ListNode(0)
        current = dummy_head
        
        # Traverse both lists
        while l1 is not None or l2 is not None or carry:
            sum = carry  # Start with the carry
            
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
                
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            
            # Update carry and the sum for the current digit
            carry = sum // 10
            sum = sum % 10
            
            # Create a new node with the digit sum and move the pointer
            current.next = ListNode(sum)
            current = current.next
        
        # The resulting linked list is now in `dummy_head.next`
        return dummy_head.next
        