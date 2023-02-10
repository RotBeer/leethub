# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [root]
        pathSum = 0
        while stack:
            root = stack.pop()
            if not root.left and not root.right and root.val == targetSum:
                return True
            if root.right:
                root.right.val += root.val
                stack.append(root.right)
            if root.left:
                root.left.val += root.val
                stack.append(root.left)

        return False