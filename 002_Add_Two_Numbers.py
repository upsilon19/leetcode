# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        k1 = l1
        k2 = l2
        k1.val += k2.val
        k1.val, remain = k1.val % 10, k1.val // 10
        while (k1.next and k2.next):
            k1 = k1.next
            k2 = k2.next
            k1.val = k1.val + k2.val + remain
            k1.val, remain = k1.val % 10, k1.val // 10

        if k2.next:
            k1.next = k2.next

        while remain != 0 and k1.next:
            k1 = k1.next
            k1.val = k1.val + remain
            k1.val, remain = k1.val % 10, k1.val // 10

        if remain != 0:
            k1.next = ListNode(remain)

        return l1
