class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # when a 1 is found find the adjacent 1s
        # count up the adjacent 1s 
        # keep track of max of which group had the most adjacent 1s

        # BFS or DFS will work fine but I think going as deep as possible might be a little more intuitive.
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        # L, R, U, D
        directions = ((-1,0), (1,0), (0,1), (0,-1))
        def dfs(i, j) :
            area = 0
            stack = deque()
            stack.append((i, j))
            # it is getting stuck somewhere in the dfs
            while stack :
                i, j = stack.pop()
                area += 1
                for direction in directions :
                    next_i = i + direction[0]
                    next_j = j + direction[1]

                    if next_i in range(rows) and next_j in range(cols) :
                        if grid[next_i][next_j] == 1 :
                            grid[next_i][next_j] = 0 # setting to 0 to mark visited
                            stack.append((next_i, next_j))
            print(area)
            return area

        for i in range(rows) :
            for j in range(cols) :
                if grid[i][j] == 1 :
                    grid[i][j] = 0
                    area = dfs(i,j)
                    max_area = max(area, max_area)
                

        return max_area
