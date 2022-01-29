/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
// DFS / RECURSIVE SOLUTION
const maxDepth = (root: TreeNode | null): number => {
  const helper = (node: TreeNode | null, i: number): number => {
    if (!node) return i;
    return Math.max(i, helper(node.left, i + 1), helper(node.right, i + 1));
  };

  return helper(root, 0);
};