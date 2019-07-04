class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        elif x != 0 and x % 10 == 0: 
            return False
        
        y = 0
        while y < x:
            y = y * 10 + x % 10
            x = x // 10
        
        return y == x or x == y // 10