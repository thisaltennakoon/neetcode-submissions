class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        for i in nums:
            countDict[i] = countDict.get(i, 0) + 1
        
        ordered = sorted(countDict, key=countDict.get, reverse=True)
        return ordered[:k]