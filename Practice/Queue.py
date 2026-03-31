# Queue -> First In, First Out (FIFO) data structure

#Enqueue
from collections import deque
queue0 = deque()
queue0.append("task 1") # enqueue task 1
queue0.append("task 2") # enqueue task 2
queue0.append("task 3") # enqueue task 3


#Dequeue
queue1 = deque(["task1", "task2", "task3"])
first = queue1.popleft() # Dequeue
#print(first) # first ->  "task1"
#print(queue1) # queue becomes ["task2", "task3"]


#Peek
queue2 = deque(["First", "Second", "Third"])

#Peek at front without removing
if len(queue2) > 0:
    front_item = queue2[0]
    print(front_item)

#Size and Empty Check
queue3 = deque(["A","B","C"])
size = len(queue3)
print(f"Queue3 has {size} items")

is_empty = len(queue3) == 0
print(is_empty)


#Always check before dequeing:
if len(queue3) > 0:
    item = queue3.popleft()
    print(item)
else:
    print("Queue is empty !")
