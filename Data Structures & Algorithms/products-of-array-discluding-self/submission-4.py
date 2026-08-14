class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #hashmap to store prod by index
        products = [1] * len(nums)
        left = 1
        #loop left to right calculating products
        for i in range(0, len(nums)):
            products[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= right
            right *= nums[i]
        
        return products