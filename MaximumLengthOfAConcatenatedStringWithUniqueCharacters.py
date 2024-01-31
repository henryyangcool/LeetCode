class Solution(object):
    def maxLength(self, arr):
        right = 0
        store = []
        temp = ''
        max_length = 0
        a = generate_combinations(arr)
        while right <= len(arr):
            for i in range(len(arr)):
                temp += arr[i]
                store.append(temp)
            temp = ''
            right += 1

        ans = []
        for j in store:
            if j not in ans:
                ans.append(j)
        for i in range(len(ans)):
            if len(ans[i]) == len(set[ans[i]]):
                max(max_length, len(ans[i]))
        return max_length


def generate_combinations(chars):
    n = len(chars)
    combinations = []

    # 总共有 2^n 个组合
    for i in range(1, 2**n):
        combination = []
        for j in range(n):
            # 检查第 j 个字符是否应该包括在内
            if i & (1 << j):
                combination.append(chars[j])
        combinations.append(''.join(combination))

    return combinations

    # def maxLength(self, arr):
    #     max_length = 0
    #     stack = [""]

    #     while stack:
    #         combination = stack.pop()
    #         max_length = max(max_length, len(combination))

    #         for string in arr:
    #             if string in combination:
    #                 continue

    #             new_combination = combination + string
    #             if len(new_combination) == len(set(new_combination)):
    #                 stack.append(new_combination)

    #     return max_length


# a = Solution().maxLength(["a", "b", "c", "d", "e", "f",
#                           "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"])
a = Solution().maxLength(["cha", "r", "act", "ers"])
print(a)
