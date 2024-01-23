class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numLen = len(nums)
        ans = []
        for i in range(numLen):
            for j in range(i):
                if i != numLen and j != numLen:
                    if nums[i] + nums[j] == target:
                        ans.append(j)
                        ans.append(i)
        return ans