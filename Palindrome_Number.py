#LeetCode: https://leetcode.com/problems/palindrome-number/
#Problem: Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]