

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Solution 1
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        if len(s) != len(t):
            return False

        storage_one = {}
        storage_two = {}

        for i in range(len(s)):
            storage_one[s[i]] = storage_one.get(s[i], 0) + 1
            storage_two[t[i]] = storage_two.get(t[i], 0) + 1

        return storage_one == storage_two
