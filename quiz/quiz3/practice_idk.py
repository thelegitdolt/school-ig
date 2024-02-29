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

# class MinHeap:
#     def __init__(self):
#         self.things = []
#
#     def insert(self, item):
#         self.things.append(item)
#         self.relocate(len(self.things) - 1, True)
#
#     def remove_min(self):
#         self.things[0] = self.things.pop()
#         self.relocate(0, False)
#
#     def relocate(self, index, go_up):
#         pass
#
#     def get(self, index):
#         return self.things[index]
#
#     def has_left(self, index):
#         return MinHeap.get_left_index(index) < len(self)
#
#     def has_right(self, index):
#         return MinHeap.get_right_index(index) < len(self)
#
#     def get_left_child(self, index):
#         if self.has_left(index):
#             return self.get(MinHeap.get_left_index(index))
#
#     def get_right_child(self, index):
#         if self.has_right(index):
#             return self.get(MinHeap.get_left_index(index))
#
#     def get_root(self, index):
#         return self.get(MinHeap.get_root_index(index))
#
#     def __len__(self):
#         return self.things.__len__()
#
#     @staticmethod
#     def get_left_index(index):
#         return index * 2 + 1
#
#     @staticmethod
#     def get_right_index(index):
#         return index * 2 + 2
#
#     @staticmethod
#     def get_root_index(index):
#         return (index - 1) // 2


from sys import maxsize
class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * maxsize
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

        # Function to return the position of

    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        return pos * 2 > self.size

        # Function to swap two nodes of the heap

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

        # Function to heapify the node at pos

    def minHeapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                    # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

                    # Function to insert a node into the heap

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

            # Function to print the contents of the heap

    def print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

            # Function to build the min heap using

    # the minHeapify function
    def minHeap(self):

        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

            # Function to remove and return the minimum

    # element from the heap
    def remove(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped
