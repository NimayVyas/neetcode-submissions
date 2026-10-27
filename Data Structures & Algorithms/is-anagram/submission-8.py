class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sontainsS = {}
        containsT = {}

        i = 0
        
        while i < len(s):

            sontainsS[s[i]] = 1 + sontainsS.get(s[i], 0)
            containsT[t[i]] = 1 + containsT.get(t[i], 0)
            i += 1

        for key, value in sontainsS.items():
            if value != containsT.get(key):
                return False

        return True


        
        