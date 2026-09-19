class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        zero_count = 0
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                product *= nums[i]

        if zero_count > 1 :
            return res
        
        for i in range(len(nums)):
            if zero_count :
                res[i] = 0 if nums[i] != 0 else product
            else:
                res[i] = product // nums[i]

        return res