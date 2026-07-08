# Create a list that is 2 * len(nums)
# Using a for loop applied to nums, add the number to the 0th and 0th + n index
# by initializing an index counter and adding to it manually through each for iteration

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * 2 * len(nums)
        i = 0

        for num in nums:
            ans[i] = num
            ans[i+n] = num
            i += 1
        
        return ans