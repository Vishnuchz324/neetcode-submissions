from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        queue = deque()
        R,C = len(grid),len(grid[0])
        
        
        for r in range(R):
            for c in range(C):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                if grid[r][c]==1:
                    fresh+=1
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while queue:
            (r,c,t) = queue.popleft()
            time = max(time,t)
            for (dr,dc) in directions:
                nr,nc = r+dr,c+dc
                if (0<=nr<R) and (0<=nc<C) and grid[nr][nc]==1:
                    fresh-=1
                    grid[nr][nc]=2
                    queue.append((nr,nc,t+1))
        return time if fresh==0 else -1