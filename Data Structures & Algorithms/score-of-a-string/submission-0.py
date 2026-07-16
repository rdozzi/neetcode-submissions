# Use the "ord" function in Python

class Solution:
    def scoreOfString(self, s: str) -> int:

        n = len(s)
        final_score = 0

        for i in range(1,n):
            final_score += abs(ord(s[i])-ord(s[i-1]))
        
        return final_score


        