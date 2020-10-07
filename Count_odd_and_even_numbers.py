Number = input('Please enter a random number: ')

# str_number = str(Number)

Odd_counter = 0
Even_counter = 0

for n in Number:
    if int(n) % 2 == 0:
        Even_counter += 1
    else:
        Odd_counter += 1

print(f'There are {Even_counter} even numbers and {Odd_counter} odd numbers in your entered number')


