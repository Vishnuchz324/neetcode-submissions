from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pac = set()
        atl = set()
        
        def dfs(r,c,prev_height,visit):
            if r<0 or c<0 or r==R or c==C or heights[r][c]<prev_height or ((r,c) in visit):
                return
            visit.add((r,c))
            for (dr,dc) in directions:
                nr,nc = r+dr,c+dc
                dfs(nr,nc,heights[r][c],visit)
        
        for r in range(R):
            for c in range(C):
                if r==0 or c==0:
                    dfs(r,c,0,pac)
                if r==R-1 or c==C-1:
                    dfs(r,c,0,atl)
        res=[]
        for point in pac:
            if point in atl:
                res.append(point)
        return res



