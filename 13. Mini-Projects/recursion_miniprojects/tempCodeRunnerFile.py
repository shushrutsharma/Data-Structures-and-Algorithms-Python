x = input("Type 1 for Countdown \nType 2 for Factorial \nType 3 for Fibonacci Sequence \n: ")

if (x == 1):
    z = int(input("Enter the starting number : "))
    print(f"Counting down from {z}")
    print(recur_countdown_time(z))

elif (x == 2):
    z = int(input("Enter the value to get factorial : "))
    print(f"The value of {z}! is {factorial_recur(z)}")

elif (x == 3):
    z = int(input("Enter the number you want fibonacci value as : "))
    fib_runner(z)