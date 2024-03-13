from labs.lab8.part2.queens import solve_queens

if __name__ == '__main__':
    n = int(input('Enter a number of queens: \n'))
    solutions = solve_queens(n)
    print(f'The {n}-queens puzzle has {len(solutions)} solutions:')
    for solution in solutions:
        print(solution)

    