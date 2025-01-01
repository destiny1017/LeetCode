class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        val = 0
        for i in range(len(nums)-1):
            val -= 1
            val = max(val, nums[i])
            if val == 0:
                return False
        return True
