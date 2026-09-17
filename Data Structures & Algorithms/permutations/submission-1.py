class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result:List[List[int]]=[]
        
        def backtrack(path:List[int],used:set[int]):
            if len(path)==len(nums):
                result.append(path.copy())
            for num in nums:
                if num not in used:
                    used.add(num)
                    path.append(num)
                    backtrack(path,used)
                    used.remove(num)
                    path.pop()
        
        backtrack([],set())
        return result