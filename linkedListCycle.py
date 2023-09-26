# https://leetcode.com/problems/linked-list-cycle/description/

from typing import Optional


# To solve this question, we are using Floyd's tortoise and hare algorith
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node1

ob = Solution()
print(ob.hasCycle(node1))
