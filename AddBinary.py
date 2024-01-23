class Solution(object):
    def addBinary(self, a, b):
        ans = str(int(a) + int(b))
        ansList = []
        for i in ans:
            ansList.append(i)

        ansList.reverse()

        up = False
        for i in range(len(ansList)):
            if up:
                ansList[i] = str(int(ansList[i]) + 1)
                up = False
            if ansList[i] == '2':
                ansList[i] = '0'
                if i == len(ansList) - 1:
                    ansList.append('1')
                up = True
            elif ansList[i] == '3':
                ansList[i] = '1'
                if i == len(ansList) - 1:
                    ansList.append('1')
                up = True

        ansList.reverse()
        answer = ''
        for i in ansList:
            answer += i

        return answer
