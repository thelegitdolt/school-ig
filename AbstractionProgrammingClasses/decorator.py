def decorator(func):
    def wrapper():
        print('===================')
        func()
        print('===================')
    return wrapper

def run_times(num):
    def wrap(func):
        for i in range(num):
            func()
    return wrap

def wrap(func):
    for i in range(4):
        print(4)

@wrap
def normal_function():
    print('hi')


def login_required(func):
    def burrito(user):
        password = input("What is the password?\n")
        if password == user["password"]:
            func(user)
        else:
            print("Access Denied!")
    return burrito

usar = dict(name='Jess', password='Hello Gamer', credit_card_number='1111111')

@login_required
def restricted_function(user):
    print("Your credit card number is " + user["credit_card_number"])

restricted_function(usar)

