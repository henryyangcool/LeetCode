class Solution(object):
    def divide(self, dividend, divisor):
        ans = dividend // divisor
        if ans > 2 ** 31 - 1:
            ans = 2 ** 31 - 1
        elif ans < -2 ** 31:
            ans = -2 ** 31

        if dividend > 0 and divisor < 0:
            ans = -(dividend // -divisor)
        elif dividend < 0 and divisor > 0:
            ans = -(-dividend // divisor)
        return ans
