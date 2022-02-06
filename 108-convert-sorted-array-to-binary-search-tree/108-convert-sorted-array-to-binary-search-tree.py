# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binarySearch(left: int, right: int) -> [TreeNode]:
            if left == right:
                return TreeNode(nums[left])
            mid = (left + right)//2
            node = TreeNode(nums[mid])
            if mid > left:
                node.left = binarySearch(left, mid-1)
            if mid < right:
                node.right = binarySearch(mid+1, right)
            return node
        return binarySearch(0, len(nums)-1)