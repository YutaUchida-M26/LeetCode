#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        dep = 0
        stack = [(root, 1)]
        while stack:
            root, length = stack.pop()
            if length > dep:
                dep = length
            if root.left != None:
                stack.append((root.left, length + 1))
            if root.right != None:
                stack.append((root.right, length + 1))
        return dep
            
# @lc code=end

