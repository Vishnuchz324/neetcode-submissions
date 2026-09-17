class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results:List[str]=[]
        def backtrack(open_count:int,close_count:int,path:str):
            if len(path)==2*n:
                results.append(path)
            if open_count<n:
                backtrack(open_count+1,close_count,path+'(')
            if close_count<open_count:
                 backtrack(open_count,close_count+1,path+')')
        backtrack(0,0,"")
        return results

