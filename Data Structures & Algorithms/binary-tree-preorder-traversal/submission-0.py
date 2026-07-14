# Classic Recursive Pattern: Read value, move left, move right.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ans = []

        def recursive_helper(root):

            if not root:
                return
            
            ans.append(root.val)
            recursive_helper(root.left)
            recursive_helper(root.right)

        recursive_helper(root)

        return ans

        