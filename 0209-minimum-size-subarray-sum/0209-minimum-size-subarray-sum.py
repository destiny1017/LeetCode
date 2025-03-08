class Solution(object):
    def minSubArrayLen(self, target, nums):
        result = 10 ** 6
        st, ed = 0, 0
        value = nums[0]
        while ed >= st:
            if value < target:
                ed += 1
                if ed == len(nums):
                    break
                value += nums[ed]
            else:
                result = min(result, ed - st + 1)
                value -= nums[st]
                st += 1
        
        return 0 if result == 10 ** 6 else result
        