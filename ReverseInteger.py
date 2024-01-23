from math import pow
class Solution:
    def reverse(self, x):
        if x < 10 and x >= 0:
            return x
        elif x > 0:
            ans = ''
            x_temp = reversed(str(x))
            for i in x_temp:
                ans += i
            if int(ans) >= int(pow(2,31) - 1):
                return 0
            else:
                return int(ans)
        elif x < 0:   
            x = abs(x)
            ans = ''
            x_temp = reversed(str(x))
            for i in x_temp:
                ans += i
            if -int(ans) <= -int(pow(2,31)):
                return 0
            else:
                return int('-' + str(ans))