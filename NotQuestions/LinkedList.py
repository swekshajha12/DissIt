class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

current = node1
while current is not None:
    print(current.value)
    current = current.next