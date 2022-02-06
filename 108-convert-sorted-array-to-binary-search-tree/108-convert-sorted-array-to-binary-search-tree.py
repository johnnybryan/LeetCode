# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    #     def binarySearch(left: int, right: int) -> [TreeNode]:
    #         if left == right:
    #             return TreeNode(nums[left])
    #         mid = (left + right)//2
    #         node = TreeNode(nums[mid])
    #         if mid > left:
    #             node.left = binarySearch(left, mid-1)
    #         if mid < right:
    #             node.right = binarySearch(mid+1, right)
    #         return node
    #     return binarySearch(0, len(nums)-1)
    #################
	  # recursive dfs #
	  #################
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    #################
	  # iterative dfs #
	  #################
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         if not nums:
#             return None

#         root = TreeNode()
#         # (node, lower, upper) with [lower, upper)
#         stack = [(root, 0, len(nums))]
        
#         while stack:
#             node, lower, upper = stack.pop()
#             mid = (lower + upper) // 2
#             node.val = nums[mid]
#             node.left = TreeNode() if mid > lower else None
#             node.right = TreeNode() if upper > mid + 1 else None
#             if node.right: stack.append((node.right, mid+1, upper))
#             if node.left: stack.append((node.left, lower, mid))
                
#         return root