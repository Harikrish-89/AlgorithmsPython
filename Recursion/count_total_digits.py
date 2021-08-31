def count_total_digits(n):
    if n%10 == n:
        return 1
    return count_total_digits(n//10) + 1

print(count_total_digits(1245))
