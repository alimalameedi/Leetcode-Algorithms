from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Solution 1
        # Time Complexity: O(m * n) m = number of strings, n = number of characters of all strings
        # Space Complexity: O(n)
        # Notes:
        #       We use an array that essentially represents every letter from a - z.
        #       to find the index of a given letter, do ord(char) - ord('a'). Add 1 to that spot.
        #       All anagrams will have the same final composition of chars/frequencies.

        storage = {}

        for s in strs:

            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            comparator = tuple(count)
            if comparator in storage:
                storage[comparator].append(s)

            else:
                storage[comparator] = [s]

        return storage.values()

        # Solution 2
        # Time Complexity: O(n^2 log n)
        # Space Complexity: O(n)
        # Notes:
        #       lists and dictionaries cannot be keys in dictionaries (maps) - they are both mutable.
        #       tuples are immutable and can be keys in dictionaries, as seen in this problem.

        # anagram_storage = {}
        # for i in range(len(strs)):
        #
        #     sorted_string = tuple(sorted(strs[i]))  # does not mutate original string
        #
        #     if sorted_string in anagram_storage:
        #         anagram_storage[sorted_string].append(strs[i])
        #     else:
        #         anagram_storage[sorted_string] = [strs[i]]
        #
        # return anagram_storage.values()
