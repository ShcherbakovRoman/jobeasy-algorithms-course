from random import randint

n = int(input('Enter number of digits: '))

first_number = 1
while n != 1:
    first_number *= 10
    n -= 1

last_number = first_number * 10 - 1
print('The range of numbers is', first_number, last_number)

number = randint(first_number, last_number)
print("Random number is", number)

result = 0
if number <= 9:
    result = number
else:
    while number > 0:
        a = number % 10
        result += a
        number = number // 10

print('The sum of all digits in random number is', result)