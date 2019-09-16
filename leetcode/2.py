# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        current_node = None
        first = None

        carry = False

        l1_finish = False
        l2_finish = False

        while True:
            if l1_finish and l2_finish:
                if carry:
                    current_node.next = ListNode(1)
                return first

            if l1_finish:
                l1_val = 0
            else:
                l1_val = l1.val

            if l2_finish:
                l2_val = 0
            else:
                l2_val = l2.val

            num = l1_val + l2_val
            if carry:
                num += 1

            if num > 9:
                carry = True
            else:
                carry = False

            new_node = ListNode(num % 10)

            if current_node is None:
                current_node = new_node
                first = new_node
            else:
                current_node.next = new_node
                current_node = current_node.next

            if l1.next is None:
                l1_finish = True
            else:
                l1 = l1.next

            if l2.next is None:
                l2_finish = True
            else:
                l2 = l2.next
