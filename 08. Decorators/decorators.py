
def my_decorator(func):
    def wrap_func():
        print("***********")
        func()
        print("***********")
    return wrap_func

@my_decorator
def hello():
    print("Hello!")

hello()

# using decorator is same as doing the below:
# my_decorator(hello)()
