import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


#A decorator function is just a function that wraps
# another function and gives another function some additional functionality.
@delay_decorator
def say_hello():
    print("Hello")


say_hello()