class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def is_palindrome(pal):
    stack = Stack()
    stack_copy = Stack()
    stack_comp = Stack()
    for char in pal:
        stack.push(char)
        stack_copy.push(char)

    while not stack.isEmpty():
        stack_comp.push(stack.pop())

    while not stack_comp.isEmpty():
        pal_char = stack_comp.pop()
        copy_char = stack_copy.pop()
        if not pal_char == copy_char:
            return False

    return True
