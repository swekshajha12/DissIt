# https://leetcode.com/problems/online-stock-span/description/?envType=study-plan-v2&envId=leetcode-75

class StockSpanner:
    def __init__(self):
        self.stack = []  # stack of tuples having price and span

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return self.stack[-1][1]


# Example usage:
stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # Output: 1
print(stockSpanner.next(80))  # Output: 1
print(stockSpanner.next(60))  # Output: 1
print(stockSpanner.next(70))  # Output: 2
print(stockSpanner.next(60))  # Output: 1
print(stockSpanner.next(75))  # Output: 4
print(stockSpanner.next(85))  # Output: 6

#
# def __init__(self):
#     self.stack = []  # Initialize an empty stack to store price and span pairs.
#
#
# def next(self, price):
#     span = 1  # Default span is 1 (the current day itself).
#
#     # While the stack is not empty and the previous prices are less than or equal to the current price,
#     # pop elements from the stack and add their spans to the current span.
#     while self.stack and price >= self.stack[-1][0]:
#         _, prev_span = self.stack.pop()
#         span += prev_span
#
#     # Push the current price and span onto the stack.
#     self.stack.append((price, span))
#
#     return span
