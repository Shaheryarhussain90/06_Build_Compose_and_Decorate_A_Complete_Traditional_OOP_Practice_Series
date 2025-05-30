
def log_function_call(func):
    def wrapper():
        print("function is being call")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello Shaheryar Hsusain")

say_hello()