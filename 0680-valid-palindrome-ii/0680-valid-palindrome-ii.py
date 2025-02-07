class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(substring):
            return substring == substring[::-1]
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:  
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
        
        return True
