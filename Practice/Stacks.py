# Using Python list as a stack
stack = []

# Push elements 
stack.append(10)
stack.append(20)
stack.append(30)
# Stack: [10, 20, 30] (30 is on top)

# Pop element
top = stack.pop()
print(top) # Returns 30
# Stack: [10, 20]

# Peek at top
if stack:
    top_element = stack[-1] # Returns 20 without removing
print(top_element)


if stack:
    top = stack.pop()
else:
    print("Stack is empty!")
    