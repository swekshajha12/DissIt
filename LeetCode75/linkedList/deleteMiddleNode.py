# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        slow, fast = dummy, dummy
        dummy.next = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return dummy.next


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(7)
node5 = ListNode(1)
node6 = ListNode(2)
node7 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

ob = Solution()
print(ob.deleteMiddle(node1))

current = node1
while current and current.next:
    print(current.val)
    current = current.next
