# Any item that enters the stack goes to the front of the queue
# The top of the stack is the 0th index of the non-empty queue
# The push operation should always go to the non-empty queue
# The pop operation will remove all but the zeroth index of the populated stack.
# The queue can then be define as empty
# The empty operation should measure the length of both queues 
# Time Complexity O(n), Space Complexity O(n)

class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        if(not self.q1 and not self.q2):
            self.q1.insert(0,x)
        elif(self.q1 and not self.q2):
            self.q1.insert(0,x)
        elif(self.q2 and not self.q1):
            self.q2.insert(0,x)
        
    def pop(self) -> int:
        if(not self.q1 and self.q2):
            for i in range(len(self.q2)-1,0,-1):
                self.q1.insert(0,self.q2[i])
            pop_value = self.q2[0]
            print("q1",len(self.q1))
            self.q2.clear()
            return pop_value
        if(self.q1 and not self.q2):
            for i in range(len(self.q1)-1,0,-1):
                self.q2.insert(0,self.q1[i])
            pop_value = self.q1[0]
            print("q2",len(self.q2))
            self.q1.clear()
            return pop_value
        
    def top(self) -> int:
        if(not self.q1 and self.q2):
            return self.q2[0]
        elif(self.q1 and not self.q2):
            return self.q1[0]        

    def empty(self) -> bool:
        return len(self.q1) + len(self.q2) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()