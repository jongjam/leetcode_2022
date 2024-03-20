class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def boundsCheck(m, n) :
            return m in range(len(grid)) and n in range(len(grid[0]))

        # L, R, U, D
        directions = [(-1, 0) ,(1, 0), (0, 1), (0, -1)] 

        def dfs(i, j) :
            stack = deque()
            stack.append((i, j))
            while stack:
                row, col = stack.pop()
                for dir_i, dir_j in directions:
                    neighbor_i, neighbor_j = dir_i + row, dir_j + col
                    if boundsCheck(neighbor_i, neighbor_j) :
                        if grid[neighbor_i][neighbor_j] == "1" :
                            grid[neighbor_i][neighbor_j] = "0"
                            stack.append((neighbor_i, neighbor_j))

        islands = 0
        for i in range(len(grid)) :
            for j in range(len(grid[i])):
                spot = grid[i][j]
                if spot == "1" :
                    dfs(i, j) # every neighboring 1 will be changed to a 0 to remove it from further checks
                    islands += 1

        print(grid)
        return islands
