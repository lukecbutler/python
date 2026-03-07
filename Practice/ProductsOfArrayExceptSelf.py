'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
'''
def productsOfArrayExceptSelf(nums: list[int]) -> list[int]:
    max_product = 1
    zero_count = 0
    return_array = []

    for i in nums: # Find the product of all non zero number in nums
        if i == 0:
            zero_count += 1
        if i != 0:
            max_product = max_product * i
    
    for i in nums:
        if zero_count > 1:
            return_array.append(0)
            continue
        if zero_count == 1:
            if i == 0:
                return_array.append(max_product)
                continue
            else:
                return_array.append(0)
                continue

        current_numeber = int(max_product / i)
        return_array.append(current_numeber)

    return return_array


        


if __name__ == "__main__":
    nums = [-1,0,1,2,3]
    k = 1
    print(productsOfArrayExceptSelf(nums))