# Use a hashset to omit duplicates and for O(1) lookups
# The value will be the start of a sequence if 1 minus that number doesn't exist
# Check whether 1 plus the start and progress values exist in the set
# If 1 plus doesn't exist, reset the count
# Set the max with each iteration that has a +1 value


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Edge Cases
        if(len(nums) == 1):
            return 1
        if(len(nums) == 1):
            return 0

        # Create a set to remove duplicates from the nums input
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            length = 1
            if(num - 1 not in nums_set):
                while(num + length in nums_set):
                    length += 1
            
            longest = max(longest,length)
        
        return longest
        
