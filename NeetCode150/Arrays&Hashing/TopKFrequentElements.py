'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]
'''
import heapq
def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequency_map = {} # init frequency map
    for i in nums: # Loop through nums
        if i in frequency_map: # If elment already exists as a key in map, increment value
            frequency_map[i] += 1
        else: # Else set key value to 1
            frequency_map[i] = 1

    min_heap = [] # init min heap

    for key, value in frequency_map.items(): # Loop through key and value in the frequency map
        heapq.heappush(min_heap, (value, key)) # add the value first, as it is the frequency and the min heap is being sorted by it
        if len(min_heap) > k: # If the min heap grows larger than k, pop off the top
            heapq.heappop(min_heap)

    most_common_elements = [] # init most common elements array
    for i in min_heap: # Loop through min heap
        most_common_elements.append(i[1]) # append key porion of tuple to return array

    
    return most_common_elements



if __name__ == "__main__":
    nums = [1,2,2,3,3,3]
    k = 2
    print(topKFrequent(nums, k))