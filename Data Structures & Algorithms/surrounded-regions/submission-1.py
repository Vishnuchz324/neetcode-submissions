class DSU:
    def __init__(self,n):
        self.parent:list[int]=list(range(n+1))
        self.size:list[int]=[1]*(n+1)
    
    def find_parent(self,n:int)->int:
        if self.parent[n]==n:
            return n
        self.parent[n] = self.find_parent(self.parent[n])
        return self.parent[n]

    def union(self,u:int,v:int)->bool:
        pu:int = self.find_parent(u)
        pv:int = self.find_parent(v)
        if pu==pv:
            return False
        if self.size[pu]>=self.size[pv]:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
        else:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        return True
    
    def is_connected(self,u:int,v:int)->bool:
        return self.find_parent(u)==self.find_parent(v)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board),len(board[0])
        dsu = DSU(ROWS*COLS+1)
        dummy = ROWS*COLS
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]!="O":
                    continue
                if r==0 or c==0 or r==ROWS-1 or c==COLS-1:
                    dsu.union(dummy,r*COLS+c)
                else:
                    for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr,nc = r+dr,c+dc
                        if (0<=nr<ROWS) and (0<=nc<COLS) and board[nr][nc]=="O":
                                dsu.union(r*COLS+c,nr*COLS+nc)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    if not dsu.is_connected(dummy,r*COLS+c):
                        board[r][c]="X"

