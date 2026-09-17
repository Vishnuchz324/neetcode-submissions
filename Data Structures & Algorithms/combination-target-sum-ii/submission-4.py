class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result:List[List[int]]=[]
        candidates.sort()
        self.dfs(0,target,candidates,[],result)
        return result

    def dfs(self,idx:int,target:int,nums:List[int],path:List[int],result:List[List[int]]):
        if target==0:
            result.append(path.copy())
            return

        for i in range(idx,len(nums)):
            if nums[i]>target:
                return
            if i>idx and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(i+1,target-nums[i],nums,path,result)
            path.pop()
            
