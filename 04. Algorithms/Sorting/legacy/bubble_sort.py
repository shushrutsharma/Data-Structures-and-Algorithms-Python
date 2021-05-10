def bubble_sort(arr):
    """
    Fill in this docstring to practice writing docstrings
    along with summarizing what the function does
    """
    swap_happened = True
    while swap_happened:
        print('bubble sort status: ' + str(arr))
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5] # original case
# l = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1] # worst case
# l = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10] # best case
bubble_sort(l)
