from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid),len(grid[0])
        num_islands = 0
        def bfs(x,y):
            queue = deque([(x,y)])
            grid[x][y]="0"
            while queue:
                ox,oy = queue.popleft()
                for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = ox+dr,oy+dc
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc]=="1":
                        queue.append((nr,nc))
                        grid[nr][nc]="0"
            return 
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]=="1":
                    num_islands+=1
                    bfs(i,j)
        return num_islands