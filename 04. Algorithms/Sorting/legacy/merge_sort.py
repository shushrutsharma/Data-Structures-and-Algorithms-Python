def merge_sorted(arr1,arr2):
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1

        else:
            sorted_arr.append(arr2[j])
            j += 1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1 


    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1  

    return sorted_arr

def mergersort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        return merge_sorted(l1, l2)


# xxxxxxxxxxxxxxxx Program Execution xxxxxxxxxxxxxxxx
l = [8, 6, 2, 5, 10, 13, 4, 55, 61, 23, 100]
print(divide_arr(l))
