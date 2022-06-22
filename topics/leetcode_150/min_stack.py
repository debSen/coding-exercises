import sys

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            current_min = self.stack[-1][-1]
        else:
            current_min = val
        current_min = min(current_min, val)
        self.stack.append([val, current_min])

    def pop(self) -> None:
        val = self.stack[-1][0]
        del self.stack[-1]
        return val
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()