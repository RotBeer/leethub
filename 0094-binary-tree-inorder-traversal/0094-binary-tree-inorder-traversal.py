# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = []
        output = []
        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                output.append(root.val)
                root = root.right

        return output
