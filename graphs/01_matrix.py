class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #LRUD
        ROWS = len(mat)
        COLS = len(mat[0])
        
        result = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        directions = ((-1, 0), (1,0), (0,1), (0,-1)) 
        def in_range(i, j) :
            return i in range(ROWS) and j in range(COLS)

        # find how many level traversal it takes to get to a 0
        def bfs(i, j, level) :
            q = deque()
            # appending coordinates
            q.append((i, j))
            # need a duplicate thing but every distance needs to be ....
            # find the max ???
            visited = set()
            while q :
                cur_len = len(q)
                for i in range(cur_len):
                    i, j = q.popleft()
                    for direction in directions :
                        next_i = i + direction[0]                           
                        next_j = j + direction[1]
                        if in_range(next_i, next_j) :
                            if mat[next_i][next_j] == 0 :
                                return level + 1
                            else :
                                q.append((next_i,next_j))
                level += 1

            return 0

        # if result is a 0 do not traverse over it
        # print(result[1][1])
        for i in range(len(mat)) :
            for j in range(len(mat[i])) :
                if mat[i][j] > 0 :
                    result[i][j] = bfs(i, j, 0)
        return result


