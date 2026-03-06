# Build Min Heap (Heapify)
# Time: O(n), Space: O(1)
import heapq

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

# Convert normal array into min-heap configuration
heapq.heapify(A)

# Heap Push (Insert element)
# Time: O(log n)
heapq.heappush(A, 4)

# Heap Pop (Extract min)
minimum = heapq.heappop(A)

# Heap Sort - returns sorted array
# Time: O(n log n), Space: O(n)
def heapsort(arr):
    heapq.heapify(arr) #make the array into a min heap
    length_of_array = len(arr)
    new_list = [0] * length_of_array

    for i in range(length_of_array):
        minn = heapq.heappop(arr)
        new_list[i] = minn

    return new_list


# Heap Push Pop: Time - O(log n) - pushes in an element and pops off the top element
heapq.heappushpop(A, 23)



#Build Heap from scratch: O(n log n), slower than heapify which is O(n)

C = [-5, 4, 2, 1, 7, 0, 3]

heap = []
for x in C:
    heapq.heappush(heap,x)

### Important for LeetCode ###
# Putting tuples of items on the heap
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

frequency_map = {}
for i in D:
    if i in frequency_map:
        frequency_map[i] += 1
    else:
        frequency_map[i] = 1

heap = []
for k, v in frequency_map.items():
    heapq.heappush(heap, (v,k))

print(heap)