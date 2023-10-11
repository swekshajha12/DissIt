# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        # find the middle node
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        secondHalf = slow.next
        slow.next = None

        # reverse the second half
        prev, current = None, secondHalf
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        maxSum = float('-inf')

        # keep adding the first half and second half
        while prev:
            maxSum = max(maxSum, prev.val + head.val)
            prev = prev.next
            head = head.next

        return maxSum


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(9)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

ob = Solution()
print(ob.pairSum(node1))
