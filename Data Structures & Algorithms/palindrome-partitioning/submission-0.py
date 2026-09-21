class Solution:
    def is_pallindrome(self,s:str,start:int,end:int)->bool:
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        results:List[List[str]]=[]
        self.backtrack(0,s,[],results)
        return results

    def backtrack(self,idx:int,s:str,path:List[str],results:List[List[str]]):
        if idx==len(s):
            results.append(path.copy())
            return 
        for i in range(idx,len(s)):
            if self.is_pallindrome(s,idx,i):
                path.append(s[idx:i+1])
                self.backtrack(i+1,s,path,results)
                path.pop()




