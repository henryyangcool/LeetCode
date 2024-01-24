class Solution(object):
    def convert(self, s, numRows):
        n = 2 * (numRows - 1) - 1
        orginN = n
        ans = ''
        s = [s[i] for i in range(len(s))]
        lenS = len(s)
        i = 0
        while len(ans) != lenS:
            ans += s[i]
            s.pop(i)
            for j in range(n, len(s), n):
                if n == orginN:
                    if j >= len(s):
                        break
                    ans += s[j]
                    s.pop(j)
                else:
                    if j >= len(s):
                        break
                    ans += s[j]
                    if j + 1 >= len(s):
                        s.pop(j)
                        break
                    ans += s[j + 1]
                    s.pop(j)
                    s.pop(j)
            n -= 2
        return ans
