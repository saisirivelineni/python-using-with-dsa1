class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"
    def peek(self):
        if not self.is_emoty:
            return self.stack[-1]
        return "Stack is empty"
    def is empty(self):
        return len(self.Stack)==0
    def display(self):
        print(self.stack)
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print