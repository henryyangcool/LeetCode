class Solution(object):
    def lengthOfLastWord(self, s):
        listOfString = s.split(' ')
        for i in listOfString[::-1]:
            if (i != ''):
                return len(i)
