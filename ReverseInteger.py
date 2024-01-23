from math import pow
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        elif x < 10 and x > 0:
            return x
        elif x > 0:
            count = 0
            total = 0
            x_temp = x
            while x_temp >= 1:
                x_temp /= 10
                count += 1
            x_temp = x
            count_temp = count - 1
            for i in range(count):
                total = (x_temp % 10) * pow(10,count_temp) + total
                x_temp /= 10
                x_temp = int(x_temp)
                count_temp -= 1
            if int(total) >= int(pow(2,31) - 1):
                return 0
            else:
                return int(total)
        elif x < 0:
            x = abs(x)
            count = 0
            total = 0
            x_temp = x
            while x_temp >= 1:
                x_temp /= 10
                count += 1
            x_temp = x
            count_temp = count - 1
            for i in range(count):
                total = (x_temp % 10) * pow(10,count_temp) + total
                x_temp /= 10
                x_temp = int(x_temp)
                count_temp -= 1
            total = int(total - 2 * total)
            if int(total) <= -2147483648:
                return 0
            else:
                return total