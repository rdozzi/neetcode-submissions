# Given a array of integers, we need to transform each index of the array to a
# value that is the largest value to its right, meaning the largest value to any
# index to the right of the list. The last index value in the transformation
# is -1.
# Brute force, traversing left to right, check all values to the right of the
# selected index, transform that value. Time: O(n^2), space O(1)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr) #Since we'll reference indices directly
        maxValue = -1

        for i in range(n):
            for j in range(i+1,n):
                maxValue = max(maxValue,arr[j])
            arr[i] = maxValue
            maxValue = -1
        
        arr[n-1] = -1
        

        return arr
