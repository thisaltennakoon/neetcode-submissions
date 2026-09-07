class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        for i in nums:
            if i in countDict:
                countDict[i] = countDict[i] + 1
            else:
                countDict[i] = 1
        
        ordered = sorted(countDict, key=countDict.get, reverse=True)
        return ordered[:k]