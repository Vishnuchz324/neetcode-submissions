class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result:List[List[int]] = []
        self.dfs(0,nums,[],result)
        return result

    def dfs(self,idx:int,nums:List[int],subset:List[int],result:List[List[int]]):
        if len(nums)==idx:
            result.append(subset.copy())
            return
        subset.append(nums[idx])
        self.dfs(idx+1,nums,subset,result)
        subset.pop()
        self.dfs(idx+1,nums,subset,result)

