class Solution(object):
    def maxArea(self, height):
        max_Area = 0
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width

            max_Area = max(max_Area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_Area
