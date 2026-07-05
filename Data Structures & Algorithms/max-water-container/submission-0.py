# Brute force: Exhaustively test each combination and then return the largest area (too much repetition)
# Use a two pointer algorithm where the two pointers start on opposing ends of the list
# then we calculate the area based on the difference of the indices (width) and min height
# The pointer with the smaller height is moved right, if it is the leftmost pointer, and left
# if it is the rightmost pointer

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #Edge Case
        if(len(heights) == 2):
            return min(heights[0],heights[1])

        # create two pointers
        l = 0
        r = len(heights)-1
        area_max = 0

        while(l != r):
            area = min(heights[l],heights[r]) * abs(r-l)
            area_max = max(area_max,area)

            if(heights[l] <= heights[r]):
                l += 1
            elif(heights[l] > heights[r]):
                r -= 1
            
        return area_max

        