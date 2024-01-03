# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root, subRoot):
        # FUCK FUCK FUCK FUCK FUCK
        def dfs(root, subRoot) :
            if isSameTree(root, subRoot) : return True
            if not root : return False
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
                

        def isSameTree(p, q) :        
            if not p and not q :
                return True
            if not p or not q or p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        return dfs(root, subRoot)

def main() :
   e = TreeNode(2)
   d = TreeNode(1)
   c = TreeNode(5)
   b = TreeNode(4, d, e)
   #r 
   a = TreeNode(3, b, c)
   
   sc = TreeNode(2)
   sb = TreeNode(1)
   #sr 
   sa = TreeNode(4, sb, sc)
   
   c3r = TreeNode(1, TreeNode(1))
   c3sr = TreeNode(1)
   
   sol = Solution()
   
   print(sol.isSubtree(c3r, c3sr))
   
    
main()
