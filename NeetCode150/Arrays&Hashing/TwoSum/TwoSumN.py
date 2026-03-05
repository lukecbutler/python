'''
O(n) Solution

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]
'''
def twoSum(nums: list[int], target: int) -> list[int]:
    index_map = {} # init index map
    for i in range(len(nums)): # Loop through nums to build index map
        index_map[nums[i]] = i


    for i in range(len(nums)): # Loop through nums to calculate complement and check for it in index map
        current_num = nums[i]
        complement = target - current_num
        if complement in index_map and i != index_map[complement]:
            return [i, index_map[complement]]


if __name__ == "__main__":
    nums = [3,4,5,6]
    target = 7

    print(twoSum(nums, target))



    #print(f"Expected Output: [0, 1]")
    #print(f"Actual Output: {twoSum(nums, target)}")


