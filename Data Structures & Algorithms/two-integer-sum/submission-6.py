class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''answer = []
        for i in range(0, len(nums), 1):
            for j in range(i+1, len(nums), 1):
                if (target == nums[i]+nums[j]):
                    answer.append(i)
                    answer.append(j)
                    return answer'''


        set = {}
        for i in range (0, len(nums)):
            if (target - nums[i] in set.keys()):
                return [set.get(target-nums[i]), i] 
            else:
                set[nums[i]]=i
        return 0