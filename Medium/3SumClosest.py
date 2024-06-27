class Solution(object):
    def threeSumClosest(self, nums, target):
        minDiff = float("inf")
        ans = []
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                currDiff = abs(curr - target)
                if curr == target:
                    return curr
                else:
                    if currDiff < minDiff:
                        minDiff = currDiff
                        ans.clear()
                        ans.append(nums[i])
                        ans.append(nums[left])
                        ans.append(nums[right])
                    if curr < target:
                        left += 1
                    else:
                        right -= 1
        return ans[0] + ans[1] + ans[2]



