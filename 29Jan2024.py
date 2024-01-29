class MyQueue:
    
    def __init__(self):
        self.stk1=[]
        self.stk2=[]

    def push(self, x: int) -> None:
        while(len(self.stk1)>0) :
            self.stk2.append(self.stk1.pop())
        self.stk1.append(x)
        while(len(self.stk2)>0) :
            self.stk1.append(self.stk2.pop())

    def pop(self) -> int:
        return self.stk1.pop()

    def peek(self) -> int:
        return self.stk1[-1]

    def empty(self) -> bool:
        return len(self.stk1)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()