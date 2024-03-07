from timeit import Timer

def analyze(function_name, data):
    times = []
    for datum in data:
        timer = Timer(f'{function_name}({datum.__str__()})',
                      f'from __main__ import {function_name}')
        the_time = timer.timeit(number=5)
        times.append(the_time)
    return times
