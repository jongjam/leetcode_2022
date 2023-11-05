import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        # Unique set for each row and col 
        for i in range(len(board)) :
            for j in range(len(board[i])) :
                cur = board[i][j]
                if cur == '.' :
                    continue
                if (cur in rows or 
                         cur in cols or 
                         cur in box[(i // 3, j // 3)]) :
                    return False
                rows[i].add(cur)
                cols[j].add(cur)
                box[(i // 3, j // 3)].add(cur)
                 
        
        return True
        