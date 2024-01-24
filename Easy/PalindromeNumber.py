class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            strNum = str(x)
            strNumLen = len(strNum)
            middle = int(strNumLen / 2)
            front = []
            for i in range(0, middle):
                front.append(strNum[i])
            b = strNumLen - 1
            for i in range(0, len(front)):
                if front[i] != strNum[b]:
                    return False
                b = b - 1
            return True
