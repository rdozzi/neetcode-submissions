# "../" = move up 1 (pop stack)
# "x/" = add to stack
# "./" = do nothing
# Is there an alternative data structure you could consider using?
# The first index represents the main folder, then each subsequent
# operation represents other operations moving about that folder
# To obtain the answer with a stack, take the final length of the stack
# and subtract it by 1. 
# I can't think of any specific edge cases

class Solution:
    def minOperations(self, logs: List[str]) -> int:

        s = []

        for log in logs:
            if(log == './'):
                continue
            elif(log == '../' and s):
                s.pop()
            elif(log == '../' and not s):
                continue
            else:
                s.append(log)
        
        return len(s)
        