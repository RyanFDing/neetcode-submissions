class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        product = 1
        zero = []
        for i in range (len(nums)):
            if (nums[i] == 0):
                zero.append(i)
            else:
                product = product*nums[i]
        if (len(zero) > 1):
            ret = [0]*len(nums)
            return ret
        elif (len(zero) == 1):
            for i in range(0, zero[0]):
                ret.append(0)
            ret.append(product)
            for i in range(zero[0]+1, len(nums)):
                ret.append(0)
            return ret
        for num in nums:
            ret.append(int(product/num))
        
        return ret
