import math

def init():
    print('Welcome to Calculator Program!')
    inp = None
    while inp not in ('quit', 'q'):
        inp = input('Please enter your expression here. To quit enter \'quit\' or \'q\':')


class Expression:
    operation_priority = {3: '^', 2: '/*', 1: '+-'}
    operation_apply = {
        '^': math.pow,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b
    }

    def __init__(self, operation, left=None, right=None):
        self.operation = operation
        self.left = left
        self.right = right

    def evaluate_tree(self):
        left_expr = self.left.evaluate_tree() if isinstance(self.left, Expression) else self.left
        right_expr = self.right.evaluate_tree() if isinstance(self.left, Expression) else self.left
        return Expression.operation_apply[self.operation](left_expr, right_expr)

    # def __repr__(self):
    #     return 'Expression({})'.format(self.expression)

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
                    parenthetical_expr += i
                    parsed_expression.append(Expression(parenthetical_expr[1:-1]))
                    parenthetical_expr = ''
                continue
            if is_parenthetical_mode:
                parenthetical_expr += i
                continue
            if i.isnumeric():
                number += i
                continue
            if len(number) > 0:
                parsed_expression.append(int(number))
                number = ''
            if i in '+-*/^':
                parsed_expression.append(i)
        else:
            if len(number) > 0:
                parsed_expression.append(int(number))

        return parsed_expression

    @staticmethod
    def to_expression_object(proto_expr: list):
        for i in range(3, 1, -1):
            expression_chains = []
            for j in proto_expr:
                current_chain = []
                if j in Expression.operation_priority[i]:
                    if j - 1 in expression_chains:
                        current_chain.extend(range(j, j+2))
                    else:
                        if len(current_chain) > 0:
                            expression_chains.append(current_chain)
                        current_chain = []
                        current_chain.extend(range(j-1, j+2))
            for chain in expression_chains:
                proto_expr[chain[0]:chain[-1]+1] = Expression.evaluate_expression_chain(proto_expr[chain[0]:chain[-1]+1])

        return Expression.evaluate_expression_chain(proto_expr)

    @staticmethod
    def evaluate_expression_chain(proto_expr: list):
        if len(proto_expr) < 1:
            raise AttributeError('Something broke lol')

        if len(proto_expr) == 1:
            return proto_expr[0]
        return Expression(proto_expr[1], proto_expr[0], Expression.evaluate_expression_chain(proto_expr[2:]))

