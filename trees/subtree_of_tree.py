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
            if root :
                res = dfs(root.right, subRoot) or dfs(root.left, subRoot)
                if root.val == subRoot.val :
                    return isSameTree(root, subRoot) or res # the problem here is that I can't stop here
                    # because not all values in the tree are not unique I need to keep recursing and see
                return res
            # if root is none, that means we didn't find a match the whole way through so there is no subtree in root
            return False 
            

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
   a = TreeNode(3 , b, c)
   
   sc = TreeNode(2)
   sb = TreeNode(1)
   #sr 
   sa = TreeNode(4, sb, sc)
   
   c3r = TreeNode(1, TreeNode(1))
   c3sr = TreeNode(1)
   
   sol = Solution()
   
   print(sol.isSubtree(c3r, c3sr))
   
    
main()