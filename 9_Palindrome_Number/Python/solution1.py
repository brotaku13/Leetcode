class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        
        reverse = 0
        copy = x
        while copy != 0:
            reverse *= 10
            reverse += copy % 10
            copy = copy // 10
        
        return reverse == x
            