# Brute force is imbedded for loops to exhaustively check all sums if they meet target: T: O(n^2), S: O(1)
# Sort the list and then use a left and right pointer
# Use Hashmap/Dict: Subtract the values of the list from the target and store that as difference: index in the dict
# Iterate through the list and check whether a number exists that isn't the same index as the difference. 
# Time: O(n), Space: O(n) - Sorting the solution will be less than the general time of the algorithm

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create array with number and index as the indices value
        nums_copy = []
        for i, num in enumerate(nums):
            nums_copy.append([num,i])
        
        nums_copy.sort()


        # Define pointers
        l = 0
        r = len(nums) - 1

        while(l != r):
            two_sum = nums_copy[l][0] + nums_copy[r][0]

            if(two_sum == target):
                return [min(nums_copy[l][1],nums_copy[r][1]),max(nums_copy[l][1],nums_copy[r][1])]
                break
            elif(two_sum < target):
                l += 1
            elif(two_sum > target):
                r -= 1
        
        return []

        # diff = dict()
        # n = len(nums)

        # for i in range(n):
        #     diff[target - nums[i]] = i


            