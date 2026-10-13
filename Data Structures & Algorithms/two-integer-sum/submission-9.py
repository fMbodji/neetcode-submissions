class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two-pass version
        """
        # 1st pass
        num_dict = {}
        for index, num in enumerate(nums):
            num_dict[num] = index

        # 2nd pass
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and num_dict[diff] != i:
                return [min(i, num_dict[diff]), max(i, num_dict[diff])]
        return []
        """

        # One pass version
        seen_dict = {}
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in seen_dict:
                return [seen_dict[diff], i]
            seen_dict[num] = i
        return []
            


        