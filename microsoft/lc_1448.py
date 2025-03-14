# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Takes root node of a tree of ints

        return number of nodes that are >= than all nodes in the path leading to them 
        """
        good_count = 0 #         
        good_count = self.findGoodNodes(root, root.val, good_count)
        return good_count

    def findGoodNodes(self, root, prev, good_count) :
        if root :        
            if root.val >= prev :
                good_count += 1
            prev = max(prev, root.val)
            # It doesn't make a deep copy or whatever
            good_count = self.findGoodNodes(root.left, prev, good_count)
            good_count = self.findGoodNodes(root.right, prev, good_count)

        return good_count
