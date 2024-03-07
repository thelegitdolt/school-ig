import math
from Projects.PA3.tree import ExpTree

def infix_to_postfix(infix):
    return Expression.of(infix).postorder()


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
        self.root = operation
        self.left = left
        self.right = right

    def __str__(self):
        a = self.left.__str__() if isinstance(self.left, Expression) else self.left
        b = self.right.__str__() if isinstance(self.right, Expression) else self.right
        return f'<{self.root}, {a}, {b}>'

    def preorder(self, is_root=True):
        a = self.left.preorder(False) if isinstance(self.left, ExpTree) else (
            int(self.left) if float(self.left).is_integer() else float(self.left))
        b = self.right.preorder(False) if isinstance(self.right, ExpTree) else (
            int(self.right) if float(self.right).is_integer() else float(self.right))
        if is_root:
            c = ' '
        else:
            c = ''
        return f'{self.root} {a} {b}'

    def postorder(self, is_root=True):
        a = self.left.postorder(False) if isinstance(self.left, Expression) else (
            int(self.left) if float(self.left).is_integer() else float(self.left))
        b = self.right.postorder(False) if isinstance(self.right, Expression) else (
            int(self.right) if float(self.right).is_integer() else float(self.right))
        return f'{a} {b} {self.root}'

    def inorder(self):
        a = self.left.inorder() if isinstance(self.left, Expression) else self.left
        b = self.right.inorder() if isinstance(self.right, Expression) else self.right
        return f'({a} {self.root} {b})'

    def evaluate_tree(self):
        left_expr = self.left.evaluate_tree() if isinstance(self.left, Expression) else self.left
        right_expr = self.right.evaluate_tree() if isinstance(self.right, Expression) else self.right
        return Expression.operation_apply[self.root](left_expr, right_expr)

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


def test():
    # test function 'infix_to_postfix' for simple input
    print(infix_to_postfix('(5+2)*3'))
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'

    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test function 'calculate' for simple input
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0

    # test function "infix_to_postfix' for more complex input
    assert infix_to_postfix('51+20*(4-2)^3') == '51 20 4 2 - 3 ^ * +'
    assert infix_to_postfix('(1.3+2.7)*((2.02-0.02)+1)+6.5') \
           == '1.3 2.7 + 2.02 0.02 - 1 + * 6.5 +'
    assert infix_to_postfix('((3^2-4)*(5-2))-(2^3+1)') \
           == '3 2 ^ 4 - 5 2 - * 2 3 ^ 1 + -'

    # test function 'calculate' for more complex input
    assert calculate('51+20*(4-2)^3') == 211.0
    assert calculate('(1.3+2.7)*((2.02-0.02)+1)+6.5') == 18.5
    assert calculate('((3^2-4)*(5-2))-(2^3+1)') == 6.0

    print('calculator.py runs fine')

