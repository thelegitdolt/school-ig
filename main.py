from Projects.PA3.calculator import Expression

test = '(4 + 5) * 3 + 7'
proto_expr = Expression.begin_parse(test)
print(proto_expr)
tree_maybe = Expression.to_expression_object(proto_expr)
print(tree_maybe.postorder())
print(tree_maybe.inorder())
print(tree_maybe.evaluate_tree())

