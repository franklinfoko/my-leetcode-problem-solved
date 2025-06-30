class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_half = 0
        number = x

        while number != 0:
            reversed_half = reversed_half * 10 + number %10
            number = number // 10
        
        return reversed_half == x
