class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    @staticmethod
    def parentheses_checker(text):
        s = Stack()
        for p in text:
            if p in '([{':
                s.push(p)
            else:
                if s.is_empty():
                    return False
                else:
                    if not matches(s.pop(), p):
                        return False
        return True



    @staticmethod
    def base_converter(dec_number, base):
        digits = '0123456789ABCDEF'
        remainder_stack = Stack()
        while dec_number > 0:
            rem = dec_number % base
            remainder_stack.push(rem)
            dec_number //= base

        new_str = ''
        while not remainder_stack.is_empty():
            new_str += digits[remainder_stack.pop()]




