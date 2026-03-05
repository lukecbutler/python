'''
Contains Duplicate

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

notion link: https://www.notion.so/Contains-Duplicates-3196fc6e7e988023a1a7e805b8fc72ee
'''

def hasDuplicate(nums: list[int]) -> bool:
    mySet = set()
    for element in nums:
        if element in mySet:
            return True
        else:
            mySet.add(element)

    return False


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(hasDuplicate(nums))