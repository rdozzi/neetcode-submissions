# As an initial edge case check, if the respective lengths of both words are not equal, return false
# One solution is that you can sort the words and then use a pointer to check if the characters are the same,
# if not, return false, else return true. O(n log n) for time given sort and O(1) space. Use of sorted method
# Use dict/hashmap, add letters from first word with count. Subtract count with second word. Check hashmap for non-zero values.
# Time for this is O(N) length of longest string, O(N) space to store string in hashmap
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False
        
        s_map = dict()

        for letter in s:
            if(letter not in s_map):
                s_map[letter] = 1
            else:
                s_map[letter] += 1
        
        for letter in t:
            if(letter not in s_map):
                s_map[letter] = 1
            else:
                s_map[letter] -= 1
        
        for value in s_map.values():
            if(value != 0):
                return False

        return True

        
        