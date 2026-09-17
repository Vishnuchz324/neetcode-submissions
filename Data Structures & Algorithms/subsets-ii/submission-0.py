class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results:List[List[int]]=[]
        def backtrack(idx:int,path:List[int]):
            if idx==len(nums):
                result =sorted(path)
                if result not in results:
                    results.append(result.copy())
                return
            path.append(nums[idx])
            backtrack(idx+1,path)
            path.pop()
            backtrack(idx+1,path)
        backtrack(0,[])
        return results

        