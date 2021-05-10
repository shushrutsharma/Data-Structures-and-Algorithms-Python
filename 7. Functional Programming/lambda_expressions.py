

import functools

my_list = [1,2,3,4,5]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(functools.reduce(lambda acc,item: item+acc, my_list))

'''
syntax:
lambda param: action(param)
it automatically returns the action taken,
it do not have any name, doesn't get stored in the memory.
and so used only once.
and behaves exactly like a function.
'''