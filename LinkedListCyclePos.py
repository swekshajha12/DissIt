# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional


# To solve this, we'll first floyd's turtle and hare solution first to find the cycle
# Then reset one pointer to head and move both at same speed to find the pos
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hasCycle = False
        turtle, hare = head, head

        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next

            if turtle == hare:
                hasCycle = True
                break

        if hasCycle:
            turtle = head
            while turtle != hare:
                turtle = turtle.next
                hare = hare.next

            return turtle

        return None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2


ob = Solution()
res = ob.detectCycle(node1)
print(res.val)
