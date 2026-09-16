from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = dict(Counter(nums))
    
        freq_num_list = []
        for num, count in num_dict.items(): 
            freq_num_list.append([count, num])
        freq_num_list.sort()

        res = []
        while len(res) < k:
            highest_freq_pair = (freq_num_list.pop())
            res.append(highest_freq_pair[1])
        return res

        