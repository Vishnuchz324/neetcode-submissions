class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        results:List[str]=[]
        
        def backtarck(digitIdx:int,path:str):
            if digitIdx==len(digits):
                if len(path)!=0:
                    results.append(path)
                return
            for char in letterMap[digits[digitIdx]]:
                path+=char
                backtarck(digitIdx+1,path)
                path=path[:-1]
        backtarck(0,"")
        return results


