class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result:List[List[int]] = []
        self.dfs(0,target,nums,[],result)
        return result

    def dfs(self,idx:int,target:int,nums:List[int],path:List[int],result:List[List[int]]):
        if target==0:
            result.append(path.copy())
        
        if target<0:    
            return
        
        for i in range(idx,len(nums)):
            if i>idx and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(i,target-nums[i],nums,path,result)
            path.pop()