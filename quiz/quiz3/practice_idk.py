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
        if not self.is_empty():
            return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return 'Stack({})'.format(self.items.__str__())

    def min(self):
        temp = Stack()
        min_maybe = None
        while not self.is_empty():
            a = self.pop()
            if min_maybe is None or a < min_maybe:
                min_maybe = a
            temp.push(a)

        while not temp.is_empty():
            self.push(temp.pop())

        return min_maybe

    def size(self):
        return len(self)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return 'Queue({})'.format(self.items.__str__())


q = Queue()
for i in [1, 2, 5, 6, 7, 9]:
    q.enqueue(i)

print(q)
print(1 == q.dequeue())
print(2 == q.dequeue())
print(q)

class MinHeap:
    def __init__(self):
        self.things = []

    def insert(self, item):
        self.things.append(item)
        self.relocate(len(self.things) - 1, True)

    def remove_min(self):
        self.things[0] = self.things.pop()
        self.relocate(0, False)

    def relocate(self, index, go_up):
        pass

    def get(self, index):
        return self.things[index]

    def has_left(self, index):
        return MinHeap.get_left_index(index) < len(self)

    def has_right(self, index):
        return MinHeap.get_right_index(index) < len(self)

    def get_left_child(self, index):
        if self.has_left(index):
            return self.get(MinHeap.get_left_index(index))

    def get_right_child(self, index):
        if self.has_right(index):
            return self.get(MinHeap.get_left_index(index))

    def get_root(self, index):
        return self.get(MinHeap.get_root_index(index))

    def __len__(self):
        return self.things.__len__()

    @staticmethod
    def get_left_index(index):
        return index * 2 + 1

    @staticmethod
    def get_right_index(index):
        return index * 2 + 2

    @staticmethod
    def get_root_index(index):
        return (index - 1) // 2
