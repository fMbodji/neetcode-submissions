class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num, in enumerate(nums):
            A.append([num,i])

        A.sort()
        i=0
        j=len(nums)-1
        while i < j:
            if A[i][0] + A[j][0] == target:
                pos1 = A[i][1]
                pos2 = A[j][1]
                return [min(pos1,pos2), max(pos1, pos2)]
            elif A[i][0] + A[j][0] < target:
                i+=1
            elif A[i][0] + A[j][0] > target:
                j-=1
        return []


        