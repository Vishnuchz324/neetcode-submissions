from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def dfs(r,c)->int:
            if not (0<=r<R and 0<=c<C) or grid[r][c]==0:
                return 0
            grid[r][c]=0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)


        max_area = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    area = dfs(r,c)
                    max_area = max(area,max_area)
        
        return max_area