class Node:
    def __init__(self, value, freq=1, nxt=None):
        self.value = value
        self.freq = freq
        self.next = nxt

class FreqStack:
    def __init__(self):
        self.stack = None

    def find_node(self, value):
        current = self.stack
        while current:
            if current.value == value:
                return current
            current = current.next

    def push(self, value: int) -> None:
        node = self.find_node(value)
        if node is not None:
            self.stack = Node(value, node.freq + 1, self.stack)
        else:
            self.stack = Node(value, 1, self.stack)

    def pop(self) -> int:
        if self.stack is not None:
            max_freq = 0
            current = self.stack
            while current:
                if current.freq > max_freq:
                    max_freq = current.freq
                current = current.next

            prev, current = None, self.stack
            while current:
                if current.freq == max_freq:
                    if prev:
                        prev.next = current.next
                    else:
                        self.stack = current.next
                    return current.value
                prev, current = current, current.next