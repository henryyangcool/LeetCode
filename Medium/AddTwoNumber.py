# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(0)
        l3 = temp
        a = 0
        while l1 != None or l2 != None or a != 0:
            if l1 != None:
                a += l1.val
                l1 = l1.next
            if l2 != None:
                a += l2.val
                l2 = l2.next
            temp.next = ListNode(a % 10)
            temp = temp.next
            a = a // 10
        return l3.next
