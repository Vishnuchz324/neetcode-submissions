class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        
        def backtrack(r:int,c:int,idx:int)->bool:
            if idx==len(word):
                return True
            
            if r<0 or r>=R or c<0 or c>=C or word[idx]!=board[r][c]:
                return False

            tmp = board[r][c]
            board[r][c]="#"
            found = (
                backtrack(r+1,c,idx+1) or
                backtrack(r-1,c,idx+1) or
                backtrack(r,c+1,idx+1) or
                backtrack(r,c-1,idx+1)
            )
            board[r][c]=tmp
            return found
        
        for r in range(R):
            for c in range(C):
                if backtrack(r,c,0):
                    return True
        return False
                    
