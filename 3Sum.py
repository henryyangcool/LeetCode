class Solution(object):
    def threeSum(self, nums):
        ans = []
        isNotZero = False
        for i in range(len(nums)):
            if nums[i] != 0:
                isNotZero = True
                break
            else:
                isNotZero = False
        if isNotZero:
            nums.sort()
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                left, right = i + 1, len(nums) - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s < 0:
                        left += 1
                    elif s > 0:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1            
            return ans 
        else:
            return [[0,0,0]]

a = Solution.threeSum([-1, 0, 1, 2, -1, -4])
print(a)