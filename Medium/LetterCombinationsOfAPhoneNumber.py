class Solution:
    def letterCombinations(self, digits):
        ans = ['']
        phone = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"],
                 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
        if not digits:
            return []
        for d in digits:
            newAns = []
            letter = phone[int(d)]
            for a in ans:
                for l in letter:
                    newAns.append(a + l)
                ans = newAns
        return ans