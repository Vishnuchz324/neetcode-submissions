from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        
        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c]=0
            area = 1
            while queue:
                (x,y) = queue.popleft()
                for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = x+dr,y+dc
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc]==1:
                        grid[nr][nc]=0
                        area+=1
                        queue.append((nr,nc))
            return area
        
        maxArea = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    area = bfs(r,c)
                    maxArea = max(area,maxArea)
        
        return maxArea