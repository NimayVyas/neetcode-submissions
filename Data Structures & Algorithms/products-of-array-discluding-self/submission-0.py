class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if nums.count(0) > 1: 
            return [0] * len(nums)

        product = math.prod(nums)
        product_without_0 = 1

        for num in nums:
            if num == 0:
                continue
            product_without_0 *= num
        
        res = []

        for num in nums:
            if num == 0:
                res.append(int(product_without_0))
            else:
                res.append(int(product/num))
        
        return res
                

        