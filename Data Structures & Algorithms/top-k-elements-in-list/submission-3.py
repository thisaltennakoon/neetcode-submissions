class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        
        for num, freq in count.items():
            bucket[freq].append(num)
        
        output = []
        outputCount = 0
        for i in reversed(bucket):
            for j in i:
                output.append(j)
                outputCount +=1
                if outputCount == k:
                    return output