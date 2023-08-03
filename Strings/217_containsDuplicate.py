from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Solution 1:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        storage = {}

        for val in nums:
            if val in storage:
                return True
            storage[val] = storage.get(val, 0) + 1

        return False

        # Solution 2:
        # Time: O(n log n) for sorting
        # Space: O(1)

        # nums.sort()
        # for i in range(1, len(nums)):
        #
        #     if nums[i] == nums[i - 1]:
        #         return True
        #
        # return False
