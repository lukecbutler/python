'''
Longest Consecutive Sequence - O(n)

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
'''



def LongestConsecutiveSequence(nums: list[int]) -> int:
    longest = 0
    numSet = set(nums)

    for number in nums:
        if (number - 1) not in numSet:
            length = 0
            while(number + length) in numSet:
                length += 1
                longest = max(length, longest)
    return longest


if __name__ == "__main__":
    nums = [2,20,4,10,3,4,5]
    print(LongestConsecutiveSequence(nums))