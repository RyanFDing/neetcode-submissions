class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
    #create set of nums
    #check each in set if x+1 in nums
    #if yes check x+2...
    #track max count
    #edge case: [] = 0
        if (nums == []):
            return 0
        count = 1
        maxcount = 1
        continuous = False

        for num in seen:
            x = 1
            while (num+x) in seen:
                count+=1
                x+=1
                continuous = True
            if (continuous == True):
                continuous = False
                maxcount = max(maxcount, count)
                count = 1
        return maxcount