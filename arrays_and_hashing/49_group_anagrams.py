from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # lists and dictionaries cannot be keys in dictionaries (maps) - they are both mutable.
        # tuples are immutable and can be keys in dictionaries, as seen in this problem.

        anagram_storage = {}
        for i in range(len(strs)):

            sorted_string = tuple(sorted(strs[i]))  # does not mutate original string

            if sorted_string in anagram_storage:
                anagram_storage[sorted_string].append(strs[i])
            else:
                anagram_storage[sorted_string] = [strs[i]]

        return anagram_storage.values()
