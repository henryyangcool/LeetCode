# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if (list1 == None):
            return list2
        if (list2 == None):
            return list1

        resNode = ListNode()

        # init
        if (list1.val > list2.val):
            resNode.val = list2.val
            list2 = list2.next

        else:
            resNode.val = list1.val
            list1 = list1.next

        lastNode = resNode

        # iterate to one listNode next is None
        while (list1 != None and list2 != None):

            nowNode = ListNode()
            if (list1.val > list2.val):
                nowNode.val = list2.val
                list2 = list2.next

            else:
                nowNode.val = list1.val
                list1 = list1.next

            lastNode.next = nowNode
            lastNode = nowNode

        # one linked list will have some remain node
        if (list1 != None):
            lastNode.next = list1

        else:
            lastNode.next = list2

        return resNode
