class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        # Index = frequency
        # buckets[3] contains numbers that appear 3 times
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        # Start from highest frequency
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)

                # Once we have k elements, return
                if len(result) == k:
                    return result
    
        