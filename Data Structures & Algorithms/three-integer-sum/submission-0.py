class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        res = []
        while i < j:
            current_sum = nums[i] + nums[j]
            if current_sum < target:
                i += 1
            elif current_sum > target:
                j -= 1
            else:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        for i in range (len(nums)):
            # hanlde duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = self.two_sum(nums[i+1:], -nums[i])
            for pair in pairs:
                triplet = [nums[i]] + pair
                triplet.sort()
                #print(triplet)
                triplets.add(tuple(triplet))
        return list(triplets)
        
        