class Structure:
    def __init__(self, items: list, max_size):
        self.items = items
        self.MAX_SIZE = max_size

    def add_item(self, item):
        ...

    def remove_item(self):
        ...

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.MAX_SIZE

    def show_contents(self):
        print('Contents=', self.items)


def bubble_sort(ls, start_at=0):
    if start_at < len(ls):
        current = start_at
        while current < len(ls):
            if ls[start_at] > ls[current]:
                ls[start_at], ls[current] = ls[current], ls[start_at]
            current += 1

        bubble_sort(ls, start_at + 1)

def binary_search(ls, num):
    left = 0
    right = len(ls)

    while left < right:
        mid = int((left + right) / 2)
        if mid == num:
            return mid
        elif mid > num:
            right = mid
        else:
            left = mid

class Stack(Structure):
    def __init__(self, items: list):
        super().__init__(items, 10)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        if not self.is_empty():
            item = self.items.pop()
            print('Removed', item)
        else:
            print('Cannot remove item from empty list')

    @staticmethod
    def demonstrate():
        # last in, first out
        # removes from last, add from last
        stack = Stack([1, 2, 3])
        stack.show_contents()

        print('now i\'m gonna remove....')
        stack.remove_item()
        stack.show_contents()
        print('now adding 4')

        stack.add_item(4)
        stack.show_contents()


class Queue(Structure):
    def __init__(self, items: list):
        super().__init__(items, 10)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        # last in, last out
        # removes from first, add from last
        self.items.pop(0)

    @staticmethod
    def demonstrate():
        # last in, last out
        # removes from first, add from last

        queue = Queue([1, 2, 3])
        queue.show_contents()

        print('now i\'m gonna remove....')
        queue.remove_item()
        queue.show_contents()
        print('now adding 4')

        queue.add_item(4)
        queue.show_contents()


class MyStruc3(Structure):
    def __init__(self, items):
        super().__init__(items, 20)

    def add_item(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            print('List is full: cannot add', item)

    # magic method for len()
    def __len__(self):
        return len(self.items)

    # magic method for '<' comparison, stands for 'less than'
    def __lt__(self, other):
        return len(self.items) < len(other.items)

    # magic method for '>' comparison, 'greater than'
    def __gt__(self, other):
        return len(self.items) > len(other.items)

    # magic method for '==' comparison
    def __eq__(self, other):
        return list.__eq__(self, other)
