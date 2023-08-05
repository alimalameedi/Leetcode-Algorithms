from heapq import *
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Solution 1
        # Time Complexity: O(n log n) - n = # elements in the original array
        # Space Complexity: O(n) - we store all the elements in the map, all elements in heap
        # in worst case (each number appears once)

        # Notes: Use a min heap to get the largest value by putting [val, -freq] in our heap.
        #           heappop(heap)
        #           heappush(heap, [val, -freq]
        #           Make an ordinary array and use above operations.
        # Undo negative to get the actual frequency for a value.

        heap, storage = [], {}

        for val in nums:
            storage[val] = storage.get(val, 0) + 1

        for val in storage:
            heappush(heap, [-storage[val], val])

        final = []
        for i in range(k):
            final.append(heappop(heap)[1])

        return final

        # Solution 2
        # Time Complexity: O(n * constant 'k') = O(n) where n = # elements in the original array
        # Space Complexity: O(n) - we store all the elements in our map

        # Notes:

        # bucket = [[] for _ in range(len(nums))]
        # cache = {}
        #
        # for val in nums:
        #     cache[val] = cache.get(val, 0) + 1
        #
        #
        # for number in cache:
        #     bucket[cache[number] - 1].append(number)
        #
        # arr = []
        # bucketPointer = len(bucket) - 1
        # while k > 0:
        #
        #     if len(bucket[bucketPointer]) == 0:
        #         bucketPointer -= 1
        #         continue
        #
        #     for element in bucket[bucketPointer]:
        #         arr.append(element)
        #         k -= 1
        #
        #     bucketPointer -= 1
        #
        # return arr

