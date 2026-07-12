# Brute Force solution. The one I implemented using two stacks
# and moving the information back and fourth for the pop method
# Push O(1), Pop O(N),Peek O(1), Empty O(1)

# Amortized version: For each pop and peek, remove all of the values
# from s1 once in reversed order and transfer to s2. Then either
# pop s2 or check the peek of s

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:

        self._transfer()
        return self.s2.pop()

        # n = len(self.s1)
        # for i in range(n-1,0,-1):
        #     self.s2.append(self.s1[i])
        
        # pop_var = self.s1[0]
        # self.s1.clear()
        # m = len(self.s2)

        # for j in range(m-1,-1,-1):
        #     self.s1.append(self.s2[j])
        
        # self.s2.clear()

        # return pop_var

    def peek(self) -> int:

        self._transfer()
        return self.s2[-1]
        

    def empty(self) -> bool:

        return len(self.s1) + len(self.s2) == 0
    
    def _transfer(self) -> None:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()