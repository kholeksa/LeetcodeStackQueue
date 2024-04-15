class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        self.head = Node(x, self.head)
    
    def pop(self):
        if self.head:
            result = self.head.value
            self.head = self.head.next
            return result

    def is_empty(self) -> bool:
        return not self.head

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.head.value

    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()
