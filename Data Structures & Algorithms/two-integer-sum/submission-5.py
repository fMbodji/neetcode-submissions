class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            num_dict[num] = i
        
        i == 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_dict and num_dict[diff] != i:
                return [i, num_dict[diff]]
            else:
                i += 1
        return []


        