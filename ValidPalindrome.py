class Solution:
    def isPalindrome(self, s : str) -> bool:
        l , r = 0, len(s) -1
        
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while l < r and not self.isAlphaNum(s[r]):
                r -=1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True
    
    
    def isAlphaNum(sefl, c ) -> bool:
        return ((ord("a") <= ord(c) <= ord("z")) or
                 (ord("A") <= ord(c) <= ord("Z")) or
                 (ord("0") <= ord(c) <= ord("9")))
    
    
if __name__ == "__main__":
    solution = Solution()
    print("LeetCode Problem 125: Valid Palindrome")
    result = solution.isPalindrome("A man, a plan, a canal: Panama")
    
    print(result)
    
    