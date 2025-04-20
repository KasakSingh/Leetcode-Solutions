#LeetCode: https://leetcode.com/problems/roman-to-integer/
#Problem: Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        total = 0
        previous_value = 0
        for char in reversed(s):
            value = roman_map[char]
            if value < previous_value:
                total -= value
            else:
                total += value
            previous_value = value
        return total