class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #LRUD
        ROWS = len(mat)
        COLS = len(mat[0])
        
        result = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        directions = ((-1, 0), (1,0), (0,1), (0,-1)) 
        def in_range(i, j) :
            return i in range(ROWS) and j in range(COLS)
        
        q = deque()

        visited = set()
        for i in range(len(mat)) :
            for j in range(len(mat[i])) :
                if mat[i][j] == 0 :
                    visited.add((i, j)) # need to add itself otherwise it will check over the 0s again
                    q.append((i, j))
        # find how many level traversal it takes to get to a 0
        
        # appending coordinates
        # need a duplicate thing but every distance needs to be ....
        while q :
            i, j = q.popleft()
                
            for direction in directions :
                next_i = i + direction[0]                           
                next_j = j + direction[1]
                if in_range(next_i, next_j) and (next_i, next_j) not in visited :
                    mat[next_i][next_j] = mat[i][j] + 1
                    visited.add((next_i, next_j)) 
                    q.append((next_i, next_j))
        return mat

