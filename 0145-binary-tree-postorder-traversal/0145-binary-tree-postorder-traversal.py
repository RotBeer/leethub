# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        output = []

        while stack:
            item = stack.pop()
            print(item)
            if item:
                output.append(item.val)
                stack.append(item.left)
                stack.append(item.right)
        
        return output[::-1]