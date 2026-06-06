class Solution:
    def isPalindrome(self, s: str) -> bool:
        #edge case empty: false


        alph="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        #edge case:
        #empty string return True
        #odd # string 0 to 8 4 is odd
        #remove non alphanumeric characters
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        #check edge case if s is only nonalphnumeric
        if (s == ""):
            return True
        
        for i in range(int(len(s)/2)):
            if (s[i].lower() != s[len(s)-i-1].lower()):
                return False
        return True