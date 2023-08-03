from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Solution 1
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        storage = {}
        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in storage:
                return [i, storage[complement]]

            storage[nums[i]] = i
