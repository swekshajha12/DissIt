'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

'''


class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Auxiliary stack to keep track of minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)  # Push the element onto the main stack

        # Update the minimum stack with the new minimum value
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()  # If the top element is the minimum, pop from the minimum stack
            self.stack.pop()  # Always pop from the main stack

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]  # Return the top element of the main stack

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]  # Return the top element of the minimum stack


# Example usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Output: -3
min_stack.pop()
print(min_stack.top())  # Output: 0
print(min_stack.getMin())  # Output: -2
