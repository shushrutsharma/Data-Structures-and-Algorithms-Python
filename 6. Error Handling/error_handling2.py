
def division_fn(num1, num2):
    try: 
        return num1/num2
    except (ZeroDivisionError, TypeError) as err:
        print(f'error: {err}')

print(division_fn(1,'0'))
print(division_fn(1,0))
print(division_fn(1,4))
