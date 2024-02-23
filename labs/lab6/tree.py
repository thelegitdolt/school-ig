class BinaryTree:
    def __init__(self, root_ob):
        self.key = root_ob
        self.left = None
        self.right = None

    def insert_left(self, item):
        if self.left is None:
            self.left = BinaryTree(item)
        else:
            new_tree = BinaryTree(item)
            new_tree.left = self.left
            self.left = new_tree

    def insert_right(self, item):
        new_tree = BinaryTree(item)
        if self.right is None:
            self.right = new_tree
        else:
            new_tree.right = self.right
            self.right = new_tree

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_root(self):
        return self.key

    def set_root(self, new_root):
        self.key = new_root

    def __str__(self):
        right = '' if self.right is None else self.right.__str__()
        left = '' if self.left is None else self.left.__str__()
        return f'{self.key}[{left}][{right}]'

    # Please use standard python naming conventions Professor Munishkina
    def insertLeft(self, item):
        self.insert_left(item)

    def insertRight(self, item):
        self.insert_right(item)

    def getRightChild(self):
        return self.get_right()

    def getLeftChild(self):
        return self.get_left()

    def getRootVal(self):
        return self.get_root()

    def setRootVal(self, new_root):
        self.set_root(new_root)
