class Solution:
    def singleNumber(self, nums):
        nums.sort()
        i = 1

        while i < len(nums):
            if nums[i - 1] == nums[i]:
                nums.pop(i)
                nums.pop(i - 1)
                i -= 1
            i += 1
        return nums[0]
