class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == -1:
                break
            
            while nums[i] == val:
                self._exchange(nums, i, cnt)
                cnt += 1
        return len(nums) - cnt
            
                
    
    def _exchange(self, nums: List[int], i: int, cnt: int):
        target = len(nums) - 1 - cnt
        nums[i] = nums[target]
        nums[target] = -1
        