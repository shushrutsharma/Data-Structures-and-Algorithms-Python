import time

def recur_countdown_time(n):
    if n == 0:
        return n
    else:
        print(n)
        time.sleep(2)
        return recur_countdown_time(n-1)

def iter_countdown_timer(n):
    while n>0:
        print(n)
        time.sleep(1)
        n -=1
    print(n)

z = int(input("Enter the starting number : "))
print(f"Counting down from {z}")
# iter_countdown_timer(z)

print(recur_countdown_time(z))