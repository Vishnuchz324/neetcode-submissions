class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result:List[List[int]]=[]
        
        def backtrack(path:List[int]):
            if len(path)==len(nums):
                result.append(path.copy())
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()
        
        backtrack([])
        return result