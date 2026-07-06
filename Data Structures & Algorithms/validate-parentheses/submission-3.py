# I can't think of how to obtain the brute force O(n^2) solution for this problem
# Could you use two pointers for this instead of a stack? Create if/else statements
#  to check compliments? No. 
# The Brute Force method, searching and replacing pairs in O(n^2) time are the
# and stack method are the only solutions to this problem
# Add the left hand brackets to the stack and remove the 

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for brk in s:
            if(brk in '({['):
                stack.append(brk)
            elif(brk == ')' and stack and stack[-1] == '('):
                stack.pop()
            elif(brk == ']' and stack and stack[-1] == '['):
                stack.pop()
            elif(brk == '}' and stack and stack[-1] == '{'):
                stack.pop()
            else:
                return False
        
        if(len(stack) == 0):
            return True
        else:
            return False





        