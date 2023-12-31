# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # this is more a BFS than it is a DFS because we want to check every node
        # doing it in a BFS fashion makes sense because it's not like we need the heights or anything
        # but doing it in a DFS should work. We don't need to perform DFS on every node and can simply
        # start from root but I will try a BFS

        queue = deque() # to use queue you append and popLeft
        queue.append([p, q])

        while queue :
            for i in range(len(queue)) :
                node = queue.popleft()
                p_node = node[0]
                q_node = node[1]
                
                if (p_node is None and q_node) or (q_node is None and p_node) :
                    print('fuck')
                    return False 
                
                # first put left and then put right
                # order of checking doesn't matter but left and right need to be added together
                if p_node and q_node :
                    if p_node.val != q_node.val :
                        return False
                    queue.append([p_node.left, q_node.left])
                    queue.append([p_node.right, q_node.right])
                
        return True
