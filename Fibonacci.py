def fibonacci(n):
    fibonacci_1 = 1
    fibonacci_2 = 1
    result = 0

    if n != 0:
        index = 0
        while index < n - 2:
            fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
            index += 1
        result = fibonacci_2

    return result

print(fibonacci(10))


