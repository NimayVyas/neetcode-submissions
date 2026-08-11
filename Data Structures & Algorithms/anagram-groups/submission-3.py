class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)

        for s in strs:
            hash = str(sorted(list(s)))
            result[hash].append(s)
    
        return list(result.values())
        