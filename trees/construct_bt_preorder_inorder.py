# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder :
            return None
        
        root = TreeNode(preorder[0]) 
        inorder_hash = dict()

        for idx, num in enumerate(preorder) : 
            inorder_hash[num] = idx              

        mid = inorder.index(preorder[0]) # you can save this in a hashamp?

        root.left = self.buildTree(preorder[1:mid + 1], inorder[: mid]) # inorder has everything in the split substrees 
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
         
                
        
