# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(4)

node1.next = node2
node2.next = node3

ob = Solution()
res = ob.deleteDuplicates(node1, )

while res is not None:
    print(res.val)
    res = res.next
