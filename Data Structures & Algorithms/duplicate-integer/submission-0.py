# I want to use a set for this. Store numbers in the set. If a number is present in the set, 
# return true, else continue on.
# O(n) time as you have to iterate through the entire list, O(n) space as it's possible that you
# store all values in a list of totally unique values
# Assume all values in the nums list are integers (valid)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        s = set()

        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        
        return False

