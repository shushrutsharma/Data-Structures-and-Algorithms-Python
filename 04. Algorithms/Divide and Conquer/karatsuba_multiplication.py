'''
    karatsuba multiplication (integer-wise)
    to multiply two n-digit integers, the following formula holds:
        => (a * c * 10^n) + (b * d) + {[(b * c) + (a * d)] * 10^(n/2)}
    where:  a = first half of first integer
            b = second half of first integer
            c = first half of second integer
            d = second half of second integer
    this can further be used with recursion to implement divide-and-conquer
    wherein each product (ac, bd, bc, ad) can be calculated using the same.

    note: assuming n = even & n1 = n2
'''
def k_multiply(x, y):
    if len(x) > 1 and len(y) > 1:                   # base condition: length of integers > 1
        a, b = x[:len(x) // 2], x[len(x) // 2:]     # divide first int for a, b, 
        c, d = y[:len(y) // 2], y[len(y) // 2:]     # divide second int for c, d

        print(a, b, c, d)
        ac = k_multiply(a, c)
        bd = k_multiply(b, d)
        bc = k_multiply(b, c)
        ad = k_multiply(a, d)
        n  = len(x)
        n2 = n // 2
        prod = (ac * pow(10, n)) + (bd) + ((bc + ad) * pow(10, n2)) # prod by karatsuba

        return prod
    else:
        return (x[0] * y[0])                  # return product if length <= 1

if __name__ == '__main__':
    try:
        first_integer = [int(x) for x in input('first integer: ')]
        second_integer = [int(x) for x in input('second integer: ')]

        if (len(second_integer) != len(first_integer)):
            raise ValueError

        prod = k_multiply(first_integer, second_integer)
        print(prod)
    except ValueError:
        print('Invalid Inputs')

