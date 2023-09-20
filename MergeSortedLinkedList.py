# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
        if list1 or list2:
            cur.next = list1 if list1 else list2

        # while dummy is not None:
        #     print(dummy.val)
        #     dummy = dummy.next

        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)


node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6

ob = Solution()
print(ob.mergeTwoLists(node1, node4))