class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        containsS, containsT = {}, {}

        for i in range(len(s)):
            containsS[s[i]] = 1 + containsS.get(s[i], 0)
            containsT[t[i]] = 1 + containsT.get(t[i], 0)

        for key, value in containsS.items():
            if value != containsT.get(key):
                return False

        return True

        
        