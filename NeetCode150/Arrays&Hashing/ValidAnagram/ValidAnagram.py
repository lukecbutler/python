'''
Valid Anagram

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false
'''
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    s_frequency_map = {} #init s frequency map

    for char in s: # loop through s and build frequency map
        if char in s_frequency_map:
            s_frequency_map[char] += 1
        else:
            s_frequency_map[char] = 1

    t_frequency_map = {} #init t frequency map
    for char in t: # loop through t and build frequency map
        if char in t_frequency_map:
            t_frequency_map[char] += 1
        else:
            t_frequency_map[char] = 1

    if s_frequency_map == t_frequency_map:
        return True
    else:
        return False


if __name__ == "__main__":
    s = "racecar"
    t = "carrace"

    print("Test Case Expectation: True\n")

    testcase = isAnagram(s,t)
    print(f"Test Case Actuality: {testcase}")