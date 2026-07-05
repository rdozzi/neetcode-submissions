class Solution:
    def isPalindrome(self, s: str) -> bool:

        if(len(s) == 1):
            return True

        # Define Recursive Algo
        def checkIfPalindrome(string: str, l: int, r: int) -> bool:
            # Base Case
            if l >= r:
                return True
            # Case if left indices is non-alphanumeric
            if not s[l].isalnum():
                return checkIfPalindrome(string, l+1,r)
            #Case if right indices in non-alphanumeric
            if not s[r].isalnum():
                return checkIfPalindrome(string,l,r-1)

            if(string[l].lower() != string[r].lower()):
                return False
            
            return checkIfPalindrome(string,l+1,r-1)
        
        return checkIfPalindrome(s,0,len(s)-1)
            


            
            


        