# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # LOR = left or right, 2 for the root of entire tree
        top_val = root.val
        # could get a min on the right
        # could get a max on the left

        # could c
        def dfs(root, min, max) :
            if root :
                if not (root.val > min and root.val < max) :
                    return False

                return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)
            return True # if it is null child, technically it is a BST

        return dfs(root, float(-inf), float(inf))
        
        # the left side of the tree should be treated different from the right side, even in BFS this has to happen
