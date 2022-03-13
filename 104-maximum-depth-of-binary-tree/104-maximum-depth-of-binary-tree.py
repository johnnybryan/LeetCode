# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;
        stack = [root]
        level = 0
        while stack:
            tempStack = []
            level += 1
            while stack:
                node = stack.pop()
                if node.left:
                    tempStack.append(node.left)
                if node.right:
                    tempStack.append(node.right)
            stack = tempStack
        return level