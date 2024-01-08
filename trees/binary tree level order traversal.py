# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # doing this with recursion is a pretty bad idea because it is a level order thing so it makes more sense to do this with bfs
        res = []

        def bfs(root) :
            q = deque() # queue, use append to add and popLeft() to remove
            q.append(root) # adding the start point
            while q : 
                level = []
                for i in range(len(q)):
                    cur = q.popleft()
                    # the easiest way to do this is add a tuple to res
                    if cur :
                        level.append(cur.val)
                        q.append(cur.left)
                        q.append(cur.right)
                if level :
                    res.append(level)
                        

                print(res)
        if root : bfs(root)
        return res
