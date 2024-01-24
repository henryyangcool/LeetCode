class Solution(object):
    def uniqueOccurrences(self, arr):
        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        occurrences = set()
        for num in count.values():
            if num in occurrences:
                return False
            occurrences.add(num)

        return True
