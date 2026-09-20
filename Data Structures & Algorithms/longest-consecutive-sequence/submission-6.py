class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(set(nums))
        print(sorted_nums)
        i, j = 0, 1
        counter = 1
        counter_list = []
        while j < len(sorted_nums):
            if abs(sorted_nums[j] - sorted_nums[i]) == 1:
                counter += 1
            else:
                counter_list.append(counter) # save current cnt
                counter = 1 # then restart counter
            i += 1
            j += 1
        counter_list.append(counter)

        return max(counter_list)
        

        