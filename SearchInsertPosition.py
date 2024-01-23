class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target > nums[-1]:
                    return len(nums)
                elif target < nums[0]:
                    return 0
                elif nums[i] < target and nums[i + 1] > target:
                    return i + 1
