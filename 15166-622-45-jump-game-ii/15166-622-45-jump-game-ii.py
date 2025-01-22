class Solution(object):
    def jump(self, nums):
        step = [10000] * len(nums)
        step[0] = 0
        for i in range(len(nums)-1):
            for j in range(i, i+nums[i]):
                if len(nums)-1 <= j:
                    break
                step[j+1] = min(step[j+1], step[i] + 1)
        
        return step[-1]