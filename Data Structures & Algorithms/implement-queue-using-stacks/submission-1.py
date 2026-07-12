class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:

        n = len(self.s1)
        for i in range(n-1,0,-1):
            self.s2.append(self.s1[i])
        
        pop_var = self.s1[0]
        self.s1.clear()
        m = len(self.s2)

        for j in range(m-1,-1,-1):
            self.s1.append(self.s2[j])
        
        self.s2.clear()

        return pop_var

    def peek(self) -> int:

        return self.s1[0]
        

    def empty(self) -> bool:

        return len(self.s1) + len(self.s2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()