
def fib(num):
    a = 0
    b= 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

num = int(input("Enter a number: "))

for i in fib(num):
    print(i)
