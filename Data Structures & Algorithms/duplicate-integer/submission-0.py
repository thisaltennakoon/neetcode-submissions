class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        out = False
        indexMap = {}
        for i in nums:
            if i in indexMap:
                out = True
                break
            else: 
                indexMap[i] = 1
        return out
        