class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS = {}
        dictT = {}

        for j in range(len(s)):
            if s[j] in dictS:
                dictS[s[j]] = dictS[s[j]] +1
            else:
                dictS[s[j]] = 1

            if t[j] in dictT:
                dictT[t[j]] = dictT[t[j]] +1
            else:
                dictT[t[j]] = 1
        return dictS == dictT