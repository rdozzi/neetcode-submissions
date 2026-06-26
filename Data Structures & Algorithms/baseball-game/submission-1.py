# Solution will always be O(n) time since you have to iterate through the entire list
# Solution will be O(N) as all answers will be stored
# Solution list will be added to make an integer
# Each operation will be documented in an if, elif, else statement
# No edge cases jump out at me
# if cases will be specific to +, C, and D, else case will be string integers
# Since the list is growing, you have to keep track of the list size and then apply that size to the solution


# Notes: Make sure you REALLY understand what the operations are asking. 
# For instruction D, you're supposed to double the score.
# Remember that to perform math operations, everything has to be 
# converted into a number

# Use negative indices when you need to grab values in reverse
# 

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []
        n = len(operations)

        for i in range(n):
            if(operations[i] == "+"):
                new_Number = record[-2] + record[-1]
                record.append(new_Number)
            elif(operations[i] == "C"):
                record.pop()
            elif(operations[i] == "D"):
                new_Number = 2 * record[-1]
                record.append(new_Number)
            else:
                record.append(int(operations[i]))
            
        return sum(record)