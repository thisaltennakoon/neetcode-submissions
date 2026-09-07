class Solution:
    def getAnagram(self, strA: str) -> tuple:
        anagramArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in strA:
            index = ord(i)-97
            anagramArr[index] = anagramArr[index] + 1
        return tuple(anagramArr)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputDict = {}
        for word in strs:
            anagramTuple = self.getAnagram(word)
            if anagramTuple in outputDict:
                outputDict[anagramTuple].append(word)
            else:
                outputDict[anagramTuple] = [word]
        return list(outputDict.values())