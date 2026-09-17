class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results:List[List[int]]=[]
        nums.sort()
        def backtrack(idx:int,path:List[int]):
            if idx>=len(nums):
                results.append(path.copy())
                return
            path.append(nums[idx])
            backtrack(idx+1,path)
            path.pop()
            while idx+1<len(nums) and nums[idx+1]==nums[idx]:
                idx+=1
            backtrack(idx+1,path)
        backtrack(0,[])
        return results

        