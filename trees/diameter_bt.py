# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # its not about going the lowest possible from root
    # its about calculating depth of left and right for every node
    
    def __init__(self) :
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # adding the left and the right ?
        
        def dfs(root) :
            left = dfs(root.left) if root.left else 0# calling dfs first allows you to checkout every node
            right = dfs(root.right) if root.right else 0# this is getting the heights below me of the left and right
            diameter = left + right  # using these for comparisons

            self.res = max(self.res, diameter)

            # returning the height
            return 1 + max(left, right) # this is returning the height
        
       
        dfs(root)
        return self.res
