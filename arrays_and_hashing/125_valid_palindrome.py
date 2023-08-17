class Solution:

    def isPalindrome(self, s: str) -> bool:

        def checkAlphaNumeric(character):
            return (ord('z') >= ord(character) >= ord('a')) or (ord('0') <= ord(character) <= ord('9'))

        # Time Complexity: O(n), where n is the size of the input string
        # Space Complexity: O(1)

        # Solution requires two pointers - we increment each pointer forward when we do not have a valid character to
        # process. We needed a helper function to avoid having too much repeated logic & having messy code here. Good
        # point to remember - always modularize and reduce when able!

        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not checkAlphaNumeric(s[l].lower()):
                l += 1

            while l < r and not checkAlphaNumeric(s[r].lower()):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
