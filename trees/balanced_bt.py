# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # finding the height
        # it is balanced if the height of the left and right do not differ by more than 1?
        if not root :
            return True
        # doing it the very first way goes the very deepest it can go
        # doing it the way I learned it yesterday spreads the work to every node
        
        # again... spread the work to every node by starting at the bottom
        # you start at the bottom by making recursive call before return statement
        # you can use numbers or other ways to to create some kind of check for boolean
        def dfs(root) :
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and
                        abs(left[1] - right[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
