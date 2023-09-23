class Solution(object):

    def find_pivot(self, start, end, target, arr):
        if start > end:
            return start
        
        mid = (start + end) // 2

        if mid > 0 and arr[mid] < arr[mid-1]:
            return mid

        if arr[mid] == target:
            return mid + 1
        elif arr[mid] > target:
            return self.find_pivot(mid+1, end, target, arr)
        elif arr[mid] < target:
            return self.find_pivot(start, mid-1, target, arr)


    def find_target(self, start, end, target, arr):
        if start > end:
            return -1
        
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return self.find_target(start, mid-1, target, arr)
        elif arr[mid] < target:
            return self.find_target(mid+1, end, target, arr)
        

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 2:
            if target in nums:
                return nums.index(target)
            else:
                return -1

        if nums[0] == target:
            return 0
        
        is_asc = nums[0] < nums[len(nums)-1]
        if is_asc:
            pivot = 0
        else:
            pivot = self.find_pivot(0, len(nums)-1, nums[0], nums)
        
        print(pivot)
        lower_arr = nums[pivot:]
        upper_arr = nums[:pivot]
        arr = lower_arr + upper_arr
        print("lower = ", lower_arr)
        print("upper = ", upper_arr)
        print(arr)
        target_index = self.find_target(0, len(arr)-1, target, arr)
        print("target_index = ", target_index)
        if target_index == -1:
            return -1
        elif is_asc:
            return target_index
        elif target < nums[0]:
            return target_index + pivot
        elif target > nums[0]:
            return target_index - len(lower_arr)
        else:
            return target_index

        
        