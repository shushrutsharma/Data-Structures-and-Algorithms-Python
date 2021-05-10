def factorial_recur(n):
    if n == 0:
        return 1
    else :
        return n*factorial_recur(n-1)

z = int(input("Enter the value to get factorial : "))
print(f"The value of {z}! is {factorial_recur(z)}")