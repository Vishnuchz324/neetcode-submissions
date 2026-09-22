from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pac = [[False]*C for _ in range(R)]
        atl = [[False]*C for _ in range(R)]
        
        def bfs(source,ocean):
            queue = deque(source)
            while queue:
                (r,c) = queue.popleft()
                ocean[r][c]=True
                for (dr,dc) in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<R and 0<=nc<C and not ocean[nr][nc]:
                        if heights[nr][nc] >= heights[r][c]:
                            queue.append((nr,nc))
        
        pac_src=[]
        atl_src=[]
        for r in range(R):
            pac_src.append((r,0))
            atl_src.append((r,C-1))
        for c in range(C):
            pac_src.append((0,c))
            atl_src.append((R-1,c))
        
        bfs(pac_src,pac)
        bfs(atl_src,atl)
        result = []
        for r in range(R):
            for c in range(C):
                if pac[r][c] and atl[r][c]:
                    result.append([r,c])
        
        return result



