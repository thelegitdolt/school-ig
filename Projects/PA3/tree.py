class BinaryTree:
    def __init__(self, root_ob, left=None, right=None):
        self.root = root_ob
        self.left = left
        self.right = right

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
        return self.root

    def set_root(self, new_root):
        self.root = new_root

    def __str__(self):
        right = '' if self.right is None else self.right.__str__()
        left = '' if self.left is None else self.left.__str__()
        return f'{self.root}({left})({right})'

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

import math

class ExpTree(BinaryTree):
    operation_priority = {3: '^', 2: '/*', 1: '+-'}
    operation_apply = {
        '^': math.pow,
        '*': lambda a, b: float(a) * float(b),
        '/': lambda a, b: float(a) / float(b),
        '+': lambda a, b: float(a) + float(b),
        '-': lambda a, b: float(a) - float(b)
    }

    def __init__(self, operation=None, left=None, right=None):
        super().__init__(operation, left, right)

    def __str__(self):
        return self.inorder()

    def preorder(self, is_root=True):
        a = self.left.preorder(False) if isinstance(self.left, ExpTree) else (
            int(self.left) if float(self.left).is_integer() else float(self.left))
        b = self.right.preorder(False) if isinstance(self.right, ExpTree) else (
            int(self.right) if float(self.right).is_integer() else float(self.right))
        if is_root:
            c = ' '
        else:
            c = ''
        return f'{self.root} {a} {b}{c}'

    def postorder(self, is_root=True):
        a = self.left.postorder(False) if isinstance(self.left, ExpTree) else (int(self.left) if float(self.left).is_integer() else float(self.left))
        b = self.right.postorder(False) if isinstance(self.right, ExpTree) else (int(self.right) if float(self.right).is_integer() else float(self.right))
        if is_root:
            c = ' '
        else:
            c = ''
        return f'{c}{a} {b} {self.root}'

    def inorder(self):
        a = self.left.inorder() if isinstance(self.left, ExpTree) else self.left
        b = self.right.inorder() if isinstance(self.right, ExpTree) else self.right
        return f'({a}{self.root}{b})'

    def evaluate_tree(self):
        left_expr = self.left.evaluate_tree() if isinstance(self.left, ExpTree) else self.left
        right_expr = self.right.evaluate_tree() if isinstance(self.right, ExpTree) else self.right
        return ExpTree.operation_apply[self.root](left_expr, right_expr)

    @staticmethod
    def make_tree(expression):
        return ExpTree.parse_postfix_weird(expression)

    @staticmethod
    def infix_to_postfix(infix):
        return ExpTree.make_tree(infix).postorder()

    def evaluate(self):
        left_expr = self.left.evaluate_tree() if isinstance(self.left, ExpTree) else self.left
        right_expr = self.right.evaluate_tree() if isinstance(self.right, ExpTree) else self.right
        return ExpTree.operation_apply[self.root](left_expr, right_expr)

    @staticmethod
    def begin_parse(expr: str):
        is_parenthetical_mode = False
        parsed_expression = []
        parenthetical_expr = ''
        parenthetical_depth = 0

        number = ''
        for i in expr:
            if i == '(':
                is_parenthetical_mode = True
                parenthetical_depth += 1
            if i == ')':
                parenthetical_depth -= 1
                if parenthetical_depth == 0:
                    is_parenthetical_mode = False
                    parsed_expression.append(ExpTree.make_tree(parenthetical_expr))
                    parenthetical_expr = ''
                else:
                    parenthetical_expr += i
                continue
            if is_parenthetical_mode:
                if not (i == '(' and parenthetical_depth == 1):
                    parenthetical_expr += i
                continue

            if i.isnumeric() or i == '.':
                number += i
                continue
            if len(number) > 0:
                parsed_expression.append(float(number))
                number = ''
            if i in '+-*/^':
                parsed_expression.append(i)
        else:
            if len(number) > 0:
                parsed_expression.append(float(number))

        return parsed_expression

    @staticmethod
    def to_expression_object(proto_expr: list):
        for priority in range(3, 1, -1):
            expression_chains = []
            current_chain = []
            for index, item in enumerate(proto_expr):
                if isinstance(item, str):
                    if item in ExpTree.operation_priority[priority]:
                        if index - 1 in expression_chains:
                            current_chain.extend(range(index, index + 2))
                        else:
                            current_chain.extend(range(index - 1, index + 2))
                    elif len(current_chain) > 0:
                        expression_chains.append(current_chain)
                        current_chain = []
            else:
                if len(current_chain) > 0:
                    expression_chains.append(current_chain)

            for chain in expression_chains:
                proto_expr[chain[0]:chain[-1] + 1] = ExpTree.convert_expression_chain(
                    proto_expr[chain[0]:chain[-1] + 1]),

        return ExpTree.convert_expression_chain(proto_expr)

    @staticmethod
    def convert_expression_chain(proto_expr: list):
        if len(proto_expr) < 1:
            raise AttributeError('Something broke lol')

        if len(proto_expr) == 1:
            return proto_expr[0]
        return ExpTree(proto_expr[1], proto_expr[0], ExpTree.convert_expression_chain(proto_expr[2:]))

    @staticmethod
    def parse_postfix(proto_expr: list):
        expr_copy = proto_expr.copy()
        ls_mod = 0
        for priority in range(3, 0, -1):
            for index, item in enumerate(proto_expr.__iter__()):
                if isinstance(item, str) and item in ExpTree.operation_priority[priority]:
                    expr_copy[index-2-ls_mod:index+1-ls_mod] = ExpTree(expr_copy[index - ls_mod],
                                                                       expr_copy[index-2-ls_mod],
                                                                       expr_copy[index-1-ls_mod]),
                    ls_mod += 2


        return expr_copy[0]

    @staticmethod
    def parse_postfix_weird(proto_expr):
        ls_mod = 0
        expr_copy = proto_expr.copy()
        for index, item in enumerate(proto_expr):
            if isinstance(item, str) and item in '+-*/^':
                expr_copy[index - 2 - ls_mod:index + 1 - ls_mod] = ExpTree(expr_copy[index - ls_mod],
                                                                           expr_copy[index - 2 - ls_mod],
                                                                           expr_copy[index - 1 - ls_mod]),
                ls_mod += 2

        return expr_copy[0]



