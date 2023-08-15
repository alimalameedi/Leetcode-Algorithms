from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Solution 1:

        # Time Complexity: O(N) - we only move through the array of size 'N' once with two pointers
        # Space Complexity: O(N) - we maintain a new array for the answer of size 'N' numbers in the array input

        prefix = 1
        postfix = 1
        arr = [1] * len(nums)
        for i in range(len(nums)):
            arr[i] *= prefix
            prefix *= nums[i]

            arr[-1 - i] *= postfix
            postfix *= nums[-1 - i]

        return arr
