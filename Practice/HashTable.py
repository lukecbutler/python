'''
Building a Hash Table from Scratch

1. Create an empty list
2. Create a hash function
3. Inserting an element using a hash function
4. Looking up an element using a hash functon
5. Handling collisions
'''

#1. Create an empty list
# my_list = [None, None, None, None, None, None, None, None, None, None] # Each of these is referred to as a bucket

#2. Create a Hash Function - sums the Unicode numbers of each character and return a number between 0 and 9
def hash_function(value):
    sum_of_characters = 0
    for char in value:
        sum_of_characters += ord(char)

    return sum_of_characters % 10

#3. Insert an Element[find the index to place an elem at, then that index becomes in the list becomes an elem]
def add(name):
    index = hash_function(name)
    my_list[index].append(name) # This is how you add to nested lists

#4. Loop up a name - input the name to find, and out comes in the index in O(1) time, the element is found by the index
def contains(name):
    index = hash_function(name)
    return my_list[index] == name

#5. Handling collisions - After implementing each bucket as a list, we can handle colisions by chaining the hashtable entries in their selected slots
my_list = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]


add("Luke")
add("Jaden")
add("Ishaan")
print(my_list)