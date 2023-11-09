class MinStack:
    # Can't you just keep min a in different variable...
    

    def __init__(self):
        self.size = 0
        self.minlocation = []
        self.stack = []
        self.minval = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minval = min(val, self.minval)
        self.minlocation.append(self.minval)
        self.size += 1

    def pop(self) -> None:
        self.stack.pop()
        self.size -= 1
        if self.size == 0 :
            self.minval = float('inf')
            self.minlocation = []
        #find new minval

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minlocation[self.size - 1]
        # how do i find a new minval after a pop
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



