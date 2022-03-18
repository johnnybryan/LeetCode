# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        maxSum = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr, prev = slow, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        while prev:
            currSum = head.val + prev.val
            maxSum = max(maxSum, currSum)
            prev = prev.next
            head = head.next
        return maxSum