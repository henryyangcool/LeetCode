class Solution(object):
    def longestPalindrome(self, s):
        # 預處理，插入'#'來統一奇偶長度的回文
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0

        for i in range(1, n - 1):
            # 利用對稱性初始化 P[i]
            P[i] = (R > i) and min(R - i, P[2 * C - i])

            # 嘗試擴展回文，更新 P[i]
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1

            # 更新中心和右邊界 R
            if i + P[i] > R:
                C, R = i, i + P[i]

        # 找到最長回文子串
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]
    
    # def longestPalindrome(self, s):
    #     T = '#'.join('{}'.format(s))
    #     P = [0] * len(T)
    #     if len(s) == 1:
    #         return s
    #     for i in range(1, len(T)):
    #         L = i - 1
    #         R = i + 1
    #         P[i] += 1
    #         while R < len(T) and T[L] == T[R]:
    #             P[i] += 1
    #             L -= 1
    #             R += 1

    #     # 找到最長回文子串
    #     maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    #     return s[(centerIndex + 2 - maxLen)//2: (centerIndex + 2 + maxLen)//2]

a = Solution().longestPalindrome('a')
# c#b#b#d
print(a)    