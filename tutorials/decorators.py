def self_printer_1():
    print('called self_printer_1')

def call_function(f):
    f()

def add_start_end_notifier(func):
    def wrapper(*args, **kwargs):
        print('Started...')
        val = func(*args, **kwargs)
        print("Ended")
        return val

    return wrapper

@add_start_end_notifier
def say_hello():
    print("Hello")

@add_start_end_notifier
def print_a_number(n: int):
    print(n)
from timeit  import Timer

Timer()

def add(x, y):
    return x + y
