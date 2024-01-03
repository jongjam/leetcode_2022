# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root.val > p.val and root.val > q.val :
            return self.lowestCommonAncestor(root.left, p, q) # if bigger than both, go left
        elif root.val < p.val and root.val < q.val :
            return self.lowestCommonAncestor(root.right, p, q)
        else :
            return root
def main() :
    # [6,2,8,0,4,7,9,null,null,3,5]
   i = TreeNode(5)
   h = TreeNode(3)
   g = TreeNode(9)
   f = TreeNode(7)
   e = TreeNode(4, h, i)
   d = TreeNode(0)
   c = TreeNode(8, g, f)
   b = TreeNode(2, d, e)
   a = TreeNode(6, b, c)
   sol = Solution()
   
   print(sol.lowestCommonAncestor(a, b, e))
   
main()
