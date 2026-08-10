class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in remainders:
                return [remainders.get(remainder), i]
            
            remainders[num] = i
        