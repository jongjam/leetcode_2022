# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        hp = []

        # n log n solution with heap

        nodes = deque()
        nodes.append(root)

        while nodes :
            for i in range(len(nodes)) :
                node = nodes.popleft()
                heapq.heappush(hp, (-node.val)) #pushing on top node
                
                if node.left : nodes.append(node.left)
                if node.right : nodes.append(node.right)
            
            while len(hp) > k :
                heapq.heappop(hp)

        return -hp[0]
        
        
        
