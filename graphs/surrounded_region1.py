class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        'O' chain that has no path to the border will be converted to X
        """

        # Because the conversion to X depends entirely on whether O is has a path to an O on the edge
        # It makes sense to start from the edges and work towards the inside
        # Could collect all i,j tuples of Os in Path from O on edge in set 
        # if (i, j) not in o_2b_ignored and board[i][j] != 'X'
        safe_o = set()

        ROWS = len(board)
        COLS = len(board[0])


        # Starting at point i, j because it is an 'O'
        # Check direction LRUD 
        # if an O and in bounds, add to o_2b_ignored 
        # skip if already in o_2b_ignored double acts as visited

        #L,R,U,D
        directions = ((-1,0),(1,0),(0,1),(0,-1))
        
        def in_bounds(i, j) :
            return i in range(ROWS) and j in range(COLS)
        
        def dfs(i, j) :
            stack = deque()
            stack.append((i, j))

            while stack :
                i, j = stack.pop()

                for direction in directions :
                    next_i = i + direction[0]
                    next_j = j + direction[1]

                    if (in_bounds(next_i, next_j) and board[next_i][next_j] == 'O' and 
                         (next_i, next_j) not in safe_o) :
                        stack.append((next_i, next_j))
                        safe_o.add((next_i, next_j))

        # Top and Bottom rows
        for i in range(COLS) :
            if board[0][i] == 'O' :
                dfs(0,i) # if there is any overlap between sides the set should handle it
            if board[ROWS - 1][i] == 'O' :
                dfs(ROWS - 1, i)

        # Left and Right columns
        for i in range(ROWS) :
            if board[i][0] == 'O' :
                dfs(i, 0)  
            if board[i][COLS - 1] == 'O' :
                dfs(i, COLS - 1)

            
        # Time limit exceeded. 
        for i in range(1, ROWS - 1) :
            for j in range(1, COLS - 1) :
                if (i, j) not in safe_o and board[i][j] != 'X' :
                    board[i][j] = 'X'                
    

        # Correct approach just have to examine the code and why not working 
        
        

