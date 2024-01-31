class Solution(object):
    def countAndSay(self, n):
        ans = []
        dicNum = dict()
        s = ''
        for i in range(1, n + 1):
            if i == 1:
                ans.append('1')
            else:
                for k in range(len(ans)):
                    if ans[k] not in dicNum:
                        dicNum[ans[k]] = 1
                    else:
                        dicNum[ans[k]] += 1

                ans = []

                for key, value in dicNum.items():
                    tempAns = str(value) + str(key)
                    ans += tempAns
                    tempAns = ''

                dicNum = {}
        for j in range(len(ans)):
            s += ans[j]
        return s


a = Solution().countAndSay(4)
print(a)
