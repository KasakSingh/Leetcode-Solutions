# LeetCode: https://leetcode.com/problems/remove-element/submissions/1613077821/
# Problem: Remove Element
# Difficulty: Easy

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
        return j
        