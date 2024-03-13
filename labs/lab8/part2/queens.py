def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
                
def solve_queens(queens_amount):
    every_perms = all_perms(list(range(1, queens_amount + 1)))
    solutions = []
    for perm in every_perms:
        is_solution = True
        # for each queen
        for column, queen in enumerate(perm):
            # for each other queen
            for offset in range(1, queens_amount):
                comp_indices = column + offset, column - offset
                # for each possible failure spots in that column
                for index in comp_indices:
                    if index < 0 or index > queens_amount - 1:
                        continue
                    if perm[index] in (queen + offset, queen - offset):
                        is_solution = False
                        break
                if not is_solution:
                    break
            if not is_solution:
                break
        if is_solution:
            solutions.append(perm)
    return solutions
                
    
