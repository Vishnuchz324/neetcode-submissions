class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid),len(grid[0])
        num_islands = 0
        def dfs(r,c):
            if r<0 or r>=R or c<0 or c>=C or grid[r][c]=="0":
                return 
            grid[r][c]="0"
            for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                dfs(nr,nc)
            return 
        for i in range(R):
            for j in range(C):
                if grid[i][j]=="1":
                    num_islands+=1
                    dfs(i,j)
        return num_islands