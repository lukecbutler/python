'''
O(n) solution

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]
'''

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    sorted_map = {}
    output_array = []

    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in sorted_map:
            sorted_map[sorted_word].append(word)
        else:
            sorted_map[sorted_word] = [word]

    for element in sorted_map:
        output_array.append(sorted_map[element])

    return output_array

if __name__ == "__main__":
    strs = ["act", "tops", "pots", "cat"]
    print(groupAnagrams(strs))
