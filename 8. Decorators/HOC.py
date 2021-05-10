
# Higher Order Function (HOC) is a function which returns another function, or accepts another function

def greet(func):
    func()
    
def greet2():
    def hello():
        print("hello!")
    return hello()

print(greet(greet2))
