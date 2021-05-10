
def my_own_forloop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

my_own_forloop([1,2,3,4,5])
