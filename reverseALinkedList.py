# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

ob = Solution()
res = ob.reverseList(node1)

while res:
    print(res.val)
    res = res.next
