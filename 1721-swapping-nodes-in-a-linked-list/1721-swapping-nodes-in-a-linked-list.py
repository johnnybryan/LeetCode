# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        first = second = None
        runner = walker = head
        
        for i in range(1, k): 
            runner = runner.next
            
        first = runner
        
        while runner.next:
            walker = walker.next
            runner = runner.next
        
        second = walker
        
        first.val, second.val = second.val, first.val
        
        return head 