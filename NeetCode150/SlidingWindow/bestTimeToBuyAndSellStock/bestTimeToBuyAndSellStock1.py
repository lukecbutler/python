'''
O(n^2)
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0
'''

def maxProfit(prices: list[int]) -> int:
    highest = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if j > i:
                if prices[j] > prices[i]:
                    highest = max(highest, prices[j] - prices[i])
    return highest
    

if __name__ == "__main__":
    print(maxProfit(prices = [5,1,5,6,7,1]))