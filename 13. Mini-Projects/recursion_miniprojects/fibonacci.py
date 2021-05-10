def fib_recur(z):
    if z == 0:
        return 0
    elif z == 1:
        return 1
    else:
        return fib_recur(z-1) + fib_recur(z-2)

def fib_runner(z):
    print(f"The {z}th number in the fibonacci sequence is {fib_recur(z)}")

z = int(input("Enter the number you want fibonacci value as : "))
fib_runner(z)