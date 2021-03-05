from sorts import quicksort, mergersort, bubblesort, insertionsort, selectionsort
import random
import time


def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return(ran_list)


def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc-tic
    print(f"Time Elapsed while {func_name.__name__.capitalize()} --> {seconds:.5f}")

size = int(input("What size of list you want to create? "))
max = int(input("What is the max value of the range? "))
run_time = int(input("How many times you want to run : "))


for num in range(run_time):
    print(f"Run : {num+1}")
    l = create_random_list(size,max)
    analyze_func(quicksort, l)
    analyze_func(mergersort, l)
    analyze_func(bubblesort, l.copy())
    analyze_func(sorted, l)
    analyze_func(insertionsort, l.copy())
    analyze_func(selectionsort, l.copy())
    print("-"*70)
