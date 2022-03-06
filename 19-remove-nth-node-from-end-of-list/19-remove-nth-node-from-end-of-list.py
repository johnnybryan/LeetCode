# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        while n > 0: # move fast pointer along n times
            fast = fast.next
            n -= 1
        if not fast: # if n is greater than list length return list
            return head.next
        while fast.next: # proceed to end of list, fast and slow n nodes apart
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # when fast reaches end, skip/remove node
        return head # return list