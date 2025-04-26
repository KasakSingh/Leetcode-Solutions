#LeetCode: https://leetcode.com/problems/single-number/submissions/
#Problem: Single Number
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num  # XOR each number
        return result