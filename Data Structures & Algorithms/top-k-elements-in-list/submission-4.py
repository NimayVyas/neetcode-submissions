class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        # Frequency
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in count.items():
            buckets[count].append(num)

        result = []

        # Return Result
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)
            
            if len(result) == k:
                return result

        