class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = collections.defaultdict(list)

        for s in strs:
            hash = str(sorted(list(s)))
            count[hash].append(s)

        return list(count.values())
        