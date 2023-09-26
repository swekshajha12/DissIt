# https://leetcode.com/problems/reorder-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # first find the mid of the linked list
        first, second = head, head
        while second.next and second.next.next:
            first = first.next
            second = second.next.next

        first_half = head
        second_half = first.next
        first.next = None

        # reverse the second half of the linked list
        prev, current = None, second_half
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        second_half = prev

        # Now, we'll link the nodes
        while second_half:
            t1, t2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = t1
            first_half, second_half = t1, t2


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

ob = Solution()
print(ob.reorderList(node1))
