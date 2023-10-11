# https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        evenHead = head.next
        odd, even = head, head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

ob = Solution()
res = ob.oddEvenList(node1)

while res:
    print(res.val)
    res = res.next
