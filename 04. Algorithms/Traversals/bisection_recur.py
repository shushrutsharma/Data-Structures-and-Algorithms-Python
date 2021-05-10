def bisection_recur(n, arr, start, stop):
    
    if start > stop: 
        return f"{n} not found in list" 

    else:
        mid = (start+stop)//2
        if n == arr[mid]:
            return f"{n} is found at index {mid}"
        
        elif n > arr[mid]:
            start = mid+1
            return bisection_recur(n, arr, start, stop)

        else:
            stop = mid-1
            return bisection_recur(n, arr, start, stop)

def create_list(max_val):
    arr = []
    for num in range(1, max_val+1):
        arr.append(num)

    return arr


max = int(input("Enter the maximum length of the list : "))
num_to_search = int(input("Enter the number you want to search for : "))
l = create_list(max)
print(l)
print(bisection_recur(num_to_search, l, 1, len(l)-1))