#COUNTDOWN TIMER :
import time 

def recur_countdown_time(n):
    if n == 0:
        return n
    else:
        print(n)
        time.sleep(1)
        return recur_countdown_time(n-1)

def iter_countdown_timer(n):
    while n>0:
        print(n)
        time.sleep(1)
        n -=1
    print(n)

#FACTORIAL : 

def factorial_recur(n):
    if n == 0:
        return 1
    else :
        return n*factorial_recur(n-1)

#FIBONACCI SEQUENCE : 

def fib_recur(z):
    if z == 0:
        return 0
    elif z == 1:
        return 1
    else:
        return fib_recur(z-1) + fib_recur(z-2)

def fib_runner(z):
    print(f"The {z}th number in the fibonacci sequence is {fib_recur(z)}")



x = int(input("Type 1 for Countdown \nType 2 for Factorial \nType 3 for Fibonacci Sequence \n: "))

if x == 1:
    z = int(input("Enter the starting number : "))
    print(f"Counting down from {z}")
    print(recur_countdown_time(z))

elif x == 2:
    z = int(input("Enter the value to get factorial : "))
    print(f"The value of {z}! is {factorial_recur(z)}")

elif x == 3:
    z = int(input("Enter the number you want fibonacci value as : "))
    fib_runner(z)