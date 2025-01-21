
class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            st, ed = i+1, len(nums)-1
            while st < ed:
                val = nums[st] + nums[ed]
                if nums[i] + val <= 0:
                    if nums[i] + val == 0:
                        result.append([nums[i], nums[st], nums[ed]])
                    
                    while st < ed and nums[st] == nums[st+1]:
                        st += 1
                    st += 1
                else:
                    while st < ed and nums[ed] == nums[ed-1]:
                        ed -= 1
                    ed -= 1
        
        return result
        