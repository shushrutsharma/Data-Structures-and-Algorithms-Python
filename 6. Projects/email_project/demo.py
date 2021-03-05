import time
from random import randint, random, seed, choice
from string import ascii_letters as letters

def bisection_iter(n, arr):
    start = 0
    stop = len(arr)-1

    while start <= stop: 
        mid = (start + stop)//2
        if n == arr[mid]:
            return mid, f"{n} found at index {mid}"  

        elif n > arr[mid]:
            start = mid+1

        else:
            stop = mid-1

    return None, f"{n} not found in list"

def analyze_func(func_name, *arr):
    tic = time.time()
    func_name(*arr)
    toc = time.time()
    seconds = toc-tic
    print(f"Time Elapsed while {func_name.__name__.capitalize()} --> {seconds:.5f}")


seed(1)
length_of_name = randint(1,15)

def generate_name ():
    seed(1)
    length_of_name = randint(1,15)
    return ''.join(choice(letters) for i in range(length_of_name))

def get_domain(list_of_domain):
    return choice(list_of_domain)

def generate_emails(list_of_domain, total_email):
    emails = []
    for num in range(total_email):
        emails.append(generate_name()+"@"+get_domain(list_of_domain))
    return emails