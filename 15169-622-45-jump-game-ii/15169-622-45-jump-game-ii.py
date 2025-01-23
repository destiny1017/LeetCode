class Solution(object):
    def jump(self, nums):
        val, i = nums[0], 0
        step = 0
        if nums[0] == 0 or len(nums) == 1:
            return 0
        
        while True:
            step += 1
            if i + val >= len(nums) - 1:
                return step
            
            now_step = val
            for j in range(now_step+1):
                if nums[i+j] > val:
                    val = nums[i+j]
                val -= 1
            i = i + now_step
            val += 1
        
        return step