class MinStack:
    # Can't you just keep min a in different variable...
    

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        curmin = self.getMin()
        if val < curmin :
            curmin = val
        self.stack.append(val)
        self.mins.append(curmin)
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        if len(self.stack) == 0 :
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.mins) == 0 :
            return float('inf')
        return self.mins[-1]
        # how do i find a new minval after a pop
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


