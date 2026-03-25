class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item) # O(1)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty Stack")
        return self.items.pop() # O(1)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty Stack")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return print(self.items)
    


myStack = Stack()
myStack.push(3)
myStack.push(2)
myStack.push(1)
myStack.display()

