class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # create a counter array for each string
            count = [0] * 26 
            # update the freq of each char in the counter arr
            for c in s:
                count[ord(c)-ord('a')] += 1
            # add to each group that have the same key, the string
            res[tuple(count)].append(s)
        
        return list(res.values())

        