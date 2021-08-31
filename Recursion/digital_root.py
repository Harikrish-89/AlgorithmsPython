def digital_root(n):
    if n%10 == n:
        return n
    return digital_root(sum_of_digits(n))

def sum_of_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


print(digital_root(5673))