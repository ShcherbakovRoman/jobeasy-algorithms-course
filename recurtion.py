# recursion for fibonacci

def rec_fib(n):
   if n <= 1:
       return n
   else:
       return (rec_fib(n-1) + rec_fib(n-2))

print(rec_fib(3))


# recursion for factorial

def rec_factorial(x):
    if x == 1:
        return x
    else:
        return x * rec_factorial(x - 1)

print(rec_factorial(5))



# recursion for digital_root

def sum_of_digits(z):
    result = 0
    for i in str(z):
        result += int(i)
    return result

def rec_digital_root(z):
    z = sum_of_digits(z)
    if z < 10:
        return z
    else:
        z = rec_digital_root(z)
    return z


print(rec_digital_root(989898))