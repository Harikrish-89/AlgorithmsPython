def fibonacci(n, memo_dict):
    if n in memo_dict:
        return memo_dict[n]
    if n <= 1:
        return n
    result = fibonacci(n-1, memo_dict) + fibonacci(n-2, memo_dict)
    memo_dict[n] = result
    return result

print(fibonacci(7, {}))
