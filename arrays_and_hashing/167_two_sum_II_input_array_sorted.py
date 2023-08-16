from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Time Complexity: O(N), where N is the # of values in the input array
        # Space Complexity: O(1)

        l, r = 0, len(numbers) - 1

        while l < r:

            valSum = numbers[l] + numbers[r]
            if valSum > target:
                r -= 1
            elif valSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
