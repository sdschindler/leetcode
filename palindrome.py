#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)
        char = []
        num = []
        for k in st:
            char.append(k)
        
        for i in reversed(st):
            num.append(i)
        
        if char == num:
            return True
        else:
            return False
