class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        p1 = 0

        while p1 < len(s):
            p2 = p1
            while s[p2] != '#':
                p2 += 1
            
            str_len = int(s[p1:p2])
            
            res.append(s[p2+1:p2+1+str_len])
            
            p1 = p2 + 1 + str_len

        return res
                


            
