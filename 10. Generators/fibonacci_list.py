
def fib(num):
    a = 0
    b= 1
    li=[]
    for i in range(num):
        li.append(a)
        temp = a
        a = b
        b = temp + b
    print(li)

num = int(input("Enter a number: "))
fib(num)
