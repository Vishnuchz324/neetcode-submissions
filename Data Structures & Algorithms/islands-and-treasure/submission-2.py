from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R,C=len(grid),len(grid[0])
        INF=2147483647
        queue=deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c]==0:
                    queue.append((r,c))

        while queue:
            (r,c)=queue.popleft()
            for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                if (0<=nr<R) and (0<=nc<C) and grid[nr][nc]==INF:
                    grid[nr][nc]=1+grid[r][c]
                    queue.append((nr,nc))