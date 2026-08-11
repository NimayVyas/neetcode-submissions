class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)

        max_len = 0

        for n in nums:
            if n - 1 in seen:
                continue
            
            cur = n
            curr_len = 0
            
            while cur in seen:
                cur += 1
                curr_len += 1
            
            max_len = max(max_len, curr_len)
        
        return max_len
            
