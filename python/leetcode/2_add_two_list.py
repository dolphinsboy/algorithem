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
        """
        i = l1
        j = l2

        head = ListNode(0)
        current = head

        while i and j:
            s = (current.val+i.val+j.val)
            current.val = s%10
            next_node = ListNode(s/10)

            i = i.next
            j = j.next
            current.next = next_node
            current = next_node

        while i:
            s = (current.val+i.val)
            current.val = s%10
            next_node = ListNode(s/10)
            i = i.next
            current.next = next_node
            current = next_node

        while j:
            s = (current.val+j.val)
            current.val = s%10
            next_node = ListNode(s/10)
            j = j.next
            current.next = next_node
            current = next_node

        current = head
        while current:
            next_node = current.next
            if next_node and next_node.next == None and next_node.val == 0:
                current.next = None
                break
            else:
                current = current.next
        return head

def main():
    #case 1
    #[1,8]
    #[0]
    #case 2
    #[9,8]
    #[1]

    l1 = ListNode(9)
    l1.next = ListNode(8)
    l2 = ListNode(1)
    s = Solution()
    head = s.addTwoNumbers(l1, l2)

    while head:
        print head.val
        head = head.next

if __name__ == '__main__':
    main()

