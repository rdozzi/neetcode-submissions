# Brute Force: Exhaustive check using nested for loops, check for conditions T: O(N^2), S: O(1)
# More Optimal: Check whether the value exists in a hashmap; if not, add to Map (value: index),
# if it is, check the indices, if that doesn't work continue on
# Edge case, a nums list of length 1 is automatically false
# T: O(N), S: O(N)


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        d = dict()

        for i,num in enumerate(nums):
            if(num in d):
                if(abs(d[num]-i) <= k):
                    return True
                else:
                    d[num] = i # Update the value
                    continue
            else:
                d[num] = i
        
        return False

        # Brute Force
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if(nums[i] == nums[j]):
        #             if(abs(i-j) <= k):
        #                 return True
        #             else:
        #                 continue
        # return False

        