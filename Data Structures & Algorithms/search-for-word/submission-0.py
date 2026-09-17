class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        
        def backtrack(r:int,c:int,idx:int,path:set[tuple[int,int]])->bool:
            if idx==len(word):
                return True
            
            if r<0 or r>=R or c<0 or c>=C or word[idx]!=board[r][c] or ((r,c) in path):
                return False

            path.add((r,c))
            found = (
                backtrack(r+1,c,idx+1,path) or
                backtrack(r-1,c,idx+1,path) or
                backtrack(r,c+1,idx+1,path) or
                backtrack(r,c-1,idx+1,path)
            )
            path.remove((r,c))
            return found
        
        for r in range(R):
            for c in range(C):
                if backtrack(r,c,0,set()):
                    return True
        return False
                    
