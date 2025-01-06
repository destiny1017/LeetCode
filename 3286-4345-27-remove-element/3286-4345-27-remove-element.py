class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        arr = []
        
        for n in nums:
            if n != val:
                arr.append(n)
        
        for i in range(len(arr)):
            nums[i] = arr[i]
        
        for i in range(len(nums) - len(arr)):
            nums.pop()
        