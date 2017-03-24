#!/usr/bin/env python

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
        将head设置为一个无用节点，返回head.next
        之前的思路是返回head
        """
        i = l1
        j = l2
        carry = 0

        head = ListNode(0)
        current = head

        while i or j or carry:
            val = 0
            if i:
                val += i.val
                i = i.next
            if j:
                val += j.val
                j = j.next
            val += carry
            carry = val/10
            current.next = ListNode(val%10)
            current = current.next
        return head.next
def main():
    #case 1
    #[1,8]
    #[0]
    #case 2
    #[9,8]
    #[1]

    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)
    s = Solution()
    head = s.addTwoNumbers(l1, l2)

    while head:
        print head.val
        head = head.next

if __name__ == '__main__':
    main()

