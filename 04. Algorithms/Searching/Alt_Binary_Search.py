# alternative binary search
# - based on "efficient iteration"
# - make jumps and slow down as we get close to target 
# - time complexity => O(logn)

# iterative
def bsearch_alt(target, arr):
    n = len(arr)
    k = 0
    i = n // 2
    while (i >= 1):
        while (k + i < n) and (arr[k + i] <= target):
            k = k + 1
        i = i // 2
    
    return k if arr[k] == target else -1



print(bsearch_alt(4, [1, 2, 3, 4, 5]))
