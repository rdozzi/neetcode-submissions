# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        ans = []

        def recursiveHelper(root):

            # Base Case
            if(not root):
                return
            
            recursiveHelper(root.left)
            ans.append(root.val)
            recursiveHelper(root.right)

        recursiveHelper(root)
        
        return ans
            





        