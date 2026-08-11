class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        p1 = 0

        while p1 < len(s):
            p2 = p1
            while s[p2] != "#":
                p2 += 1
            word_len = int(s[p1 : p2])
            res.append(s[p2 + 1: p2 + word_len + 1])
            p1 = p2 + word_len + 1
        
        return res
