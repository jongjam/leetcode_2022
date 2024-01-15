# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def backtrack(root, curStr) :
            if root :
                if root.left or root.right:
                    curStr += str(root.val) + "->"
                else :
                    curStr += str(root.val)
                    res.append(curStr)
                backtrack(root.left, curStr)
                backtrack(root.right, curStr)
            
        backtrack(root, "")
        return res
