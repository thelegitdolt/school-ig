import math
from Projects.PA3.tree import ExpTree

def infix_to_postfix(infix):
    return ExpTree.infix_to_postfix(infix)


def calculate(infix):
    return Expression.of(infix).evaluate_tree()



class Expression:
    operation_priority = {3: '^', 2: '/*', 1: '+-'}
    operation_apply = {
        '^': math.pow,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b
    }

    def __init__(self, operation=None, left=None, right=None):
        self.operation = operation
        self.left = left
        self.right = right

    def __str__(self):
        a = self.left.__str__() if isinstance(self.left, Expression) else self.left
        b = self.right.__str__() if isinstance(self.right, Expression) else self.right
        return f'<{self.operation}, {a}, {b}>'

    def preorder(self):
        a = self.left.preorder() if isinstance(self.left, Expression) else self.left
        b = self.right.preorder() if isinstance(self.right, Expression) else self.right
        return f'{self.operation} {a} {b}'

    def postorder(self):
        a = self.left.postorder() if isinstance(self.left, Expression) else self.left
        b = self.right.postorder() if isinstance(self.right, Expression) else self.right
        return f'{a} {b} {self.operation}'

    def inorder(self):
        a = self.left.inorder() if isinstance(self.left, Expression) else self.left
        b = self.right.inorder() if isinstance(self.right, Expression) else self.right
        return f'({a} {self.operation} {b})'

    def evaluate_tree(self):
        left_expr = self.left.evaluate_tree() if isinstance(self.left, Expression) else self.left
        right_expr = self.right.evaluate_tree() if isinstance(self.right, Expression) else self.right
        return Expression.operation_apply[self.operation](left_expr, right_expr)

    @staticmethod
    def of(expression: str):
        return Expression.to_expression_object(Expression.begin_parse(expression))

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
                    parsed_expression.append(Expression.of(parenthetical_expr))
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
        expression_chains = []
        for priority in range(3, 1, -1):
            current_chain = []

            for index, item in enumerate(proto_expr):
                if isinstance(item, str):
                    if item in Expression.operation_priority[priority]:
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
                proto_expr[chain[0]:chain[-1] + 1] = Expression.convert_expression_chain(
                    proto_expr[chain[0]:chain[-1] + 1]),
            expression_chains = []

        return Expression.convert_expression_chain(proto_expr)

    @staticmethod
    def convert_expression_chain(proto_expr: list):
        if len(proto_expr) < 1:
            raise AttributeError('Something broke lol')

        if len(proto_expr) == 1:
            return proto_expr[0]
        return Expression(proto_expr[1], proto_expr[0], Expression.convert_expression_chain(proto_expr[2:]))


def init():
    print('Welcome to Calculator Program!')
    inp = None
    while inp not in ('quit', 'q'):
        inp = input('Please enter your expression here. To quit enter \'quit\' or \'q\':')

        try:
            a = Expression.of(inp)
            ans = a.evaluate_tree()

            print(ans)
        except AttributeError:
            if inp in ('quit', 'q'):
                print('Goodbye!')
            else:
                print('Invalid expression!')
            continue

init()

