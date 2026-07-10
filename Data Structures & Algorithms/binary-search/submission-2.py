from typing import List

# Implement binary search
# Initialize l, r, and mid pointers where l = 0, r = len(list)-1, mid is the
# floor division of 2
# Start at the center of the sorted list, if the target is larger than the mid,
# discard lower sample space and adjust the mid to the top half. 
# If the target is smaller, discard the upper sample space and adjust the mid
# to the bottom half
# Repeat this until the target is found or the mid value equals the edges

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while(l <= r):
            mid = l +(r-l) // 2

            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                r = mid-1
            elif(nums[mid] < target):
                l = mid + 1
        
        return -1



        