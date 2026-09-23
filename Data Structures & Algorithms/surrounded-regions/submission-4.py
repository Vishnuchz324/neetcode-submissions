from collections import deque

class Solution: 
    def solve(self, board: List[List[str]]) -> None:
        ROW,COL = len(board),len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        visited=set()

        for i in range(ROW):
            if board[i][0]=="O":
                queue.append((i,0))
                visited.add((i,0))
            if board[i][COL-1]=="O":
                queue.append((i,COL-1))
                visited.add((i,COL-1))

        for j in range(1,COL-1):
            if board[0][j]=="O":
                queue.append((0,j))
                visited.add((0,j))
            if board[ROW-1][j]=="O":
                queue.append((ROW-1,j))
                visited.add((ROW-1,j))
        
        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if (0<=nr<ROW) and (0<=nc<COL) and ((nr,nc) not in visited) and board[nr][nc]=="O":
                    visited.add((nr,nc))
                    queue.append((nr,nc))

        for r in range(ROW):
            for c in range(COL):
                if board[r][c]=="O" and ((r,c) not in visited):
                    board[r][c]="X"


