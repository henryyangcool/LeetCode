class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                while right > left:
                    curr = nums[i] + nums[j] + nums[right] + nums[left]
                    if curr == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                    if curr > target:
                        right -= 1
                    else:
                        left += 1
        return sorted([list(s) for s in ans], key=lambda x: x[0])